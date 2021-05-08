import time
import cv2 
from flask import Flask, render_template, Response,request
# made changes
import numpy as np

app = Flask(__name__)
sub = cv2.createBackgroundSubtractorMOG2()  # create background subtractor

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST": 
        todo=request.form['data'] 
        print(todo) 
    """Video streaming home page."""
    return render_template('home.html')

def gen():
    """Video streaming generator function."""
    #cap = cv2.VideoCapture('http://192.168.43.117:8080/video')
    cap = cv2.VideoCapture('testing.mp4')

    # Adding coco class name --- for detection ---->
    classes = None
    with open('coco.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    # ----->
    
    # Read until video is completed
    while(cap.isOpened()):
        ret, image = cap.read()  # import image  and changing frame to image
        if not ret: #if vid finish repeat
            #image = cv2.VideoCapture("http://192.168.43.117:8080/video") # changing frame to image
            image = cv2.VideoCapture('testing.mp4')
            continue
        if ret:  # if there is a frame continue with code
            #image = cv2.resize(frame, (0, 0), None, 1, 1)  # resize image
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts image to gray
            """
                detection logic
            """

            Width = image.shape[1]
            Height = image.shape[0]
            center_of_screen=(Width//2, Height//2)
            cv2.circle(image,center_of_screen, 20, (0, 0, 255), -1) 
            net = cv2.dnn.readNet('yolov4_tiny.weights', 'yolov4_tiny.cfg')
            net.setInput(cv2.dnn.blobFromImage(image, 0.00392, (416,416), (0,0,0), True, crop=False))
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            outs = net.forward(output_layers)
            class_ids = []
            confidences = []
            boxes = []

        #create bounding box 
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.35:
                        
                        center_x = int(detection[0] * Width)
                        center_y = int(detection[1] * Height)
                        w = int(detection[2] * Width)
                        h = int(detection[3] * Height)
                        x = center_x - w / 2
                        y = center_y - h / 2
                        class_ids.append(class_id)
                        confidences.append(float(confidence))
                        boxes.append([x, y, w, h])

            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

            #check if is people detection
            for i in indices:
                i = i[0]
                box = boxes[i]
                if class_ids[i]==0:
                    label = str(classes[class_id]) 
                    cv2.rectangle(image, (round(box[0]),round(box[1])), (round(box[0]+box[2]),round(box[1]+box[3])), (0, 255, 0), 3)
                    cv2.putText(image, label, (round(box[0])-10,round(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                    center_of_detection=(round(box[0]+(box[2]/2)),round(box[1]+(box[3]/2)))
                    cv2.circle(image, center_of_detection,20,(255,0,0),-1)

        # detection logic ends ---->
            
            #cv2.imshow("countours", image)
            frame = cv2.imencode('.jpg', image)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            #time.sleep(0.1)
            key = cv2.waitKey(20)
            if key == 27:
                break

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)