import serial
from  time import sleep
import sys
import RPi.GPIO as GPIO
ser = serial.Serial('/dev/ttyACM0', 9600)


#SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BOARD)
pin_1=12
pin_2=11
pin_3=13
pin_4=15

GPIO.setup(pin_1, GPIO.OUT)
GPIO.setup(pin_2, GPIO.OUT)
GPIO.setup(pin_3, GPIO.OUT)
GPIO.setup(pin_4, GPIO.OUT)

GPIO.setwarnings(False)

delay = 0.025




def forwardStep():
    setStepper(1, 0, 1, 0)
    setStepper(0, 1, 1, 0)
    setStepper(0, 1, 0, 1)
    setStepper(1, 0, 0, 1)

def backwardStep():
    setStepper(1, 0, 0, 1)
    setStepper(0, 1, 0, 1)
    setStepper(0, 1, 1, 0)
    setStepper(1, 0, 1, 0)

def setStepper(in1, in2, in3, in4):
    GPIO.output(pin_1, in1)
    GPIO.output(pin_2, in2)
    GPIO.output(pin_3, in3)
    GPIO.output(pin_4, in4)
    time.sleep(delay)
def stopstepper():
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)





while True:
    read_serial= ser.readline()
    jay1 = read_serial
    print  ("Printing received data"+jay1) 
    
    read_serial1 = jay1.split(":")
    print "Printing array of splitted data"
    print read_serial1
    #x=(read_serial1[0])
    #y=(read_serial1[1])
    #x1=int(x)
    #y1=int(y)
    if(len(read_serial1)>=5):
        a=(read_serial1[0])
        b=(read_serial1[1])
        c=(read_serial1[2])
        x=(read_serial1[3])
        y=(read_serial1[4])
        z=(read_serial1[5])
        
#        a1=int(a)
#        b1=int(b)
#        c1=int(c)
        x1=int(x)
        y1=int(y)
        z1=int(z)
#        print(a1)
#        print(b1)
#        print(c1)
        print(x1)
        print(y1)
        print(z1)
  
    if(x1>200):            
        print("moving forward active")
        forwardStep()
            

        
    elif(x1<-200):
        print("moving backward active")
        backwardStep()
    else:
        stopstepper()
                
    if(y1<-200):
        print("P active")
        
            
    
    elif(y1>200):
        print("d active")
        
    else:
        stopstepper()
        
    
