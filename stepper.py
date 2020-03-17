import serial
from  time import sleep
import sys
import RPi.GPIO as GPIO
ser = serial.Serial('/dev/ttyACM0', 9600)

DIR = 20   # Direction GPIO Pin
STEP = 21
DIR1=19
STEP1=26
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
MODE1=(17,22,27)
GPIO.setup(MODE, GPIO.OUT)
GPIO.setup(MODE1, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['1/32'])
GPIO.output(MODE1, RESOLUTION['1/32'])
step_count = SPR * 32
delay = .0208 / 32
"""
motor_channel = (8,10,11,13)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_channel,GPIO.OUT)
"""
GPIO.setwarnings(False)


"""
P_A1 = 8  # adapt to your wiring
P_A2 = 10 # ditto
P_B1 = 11 # ditto
P_B2 = 13 # ditto
delay = 0.000
# time to settle


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_A1, GPIO.OUT)
    GPIO.setup(P_A2, GPIO.OUT)
    GPIO.setup(P_B1, GPIO.OUT)
    GPIO.setup(P_B2, GPIO.OUT)
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
    GPIO.output(P_A1, in1)
    GPIO.output(P_A2, in2)
    GPIO.output(P_B1, in3)
    GPIO.output(P0_B2, in4)
    time.sleep(delay)
def stopstepper():
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)
    setStepper(0, 0, 0, 0)

"""



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
        print("6 active")
        GPIO.output(DIR, CW)
        for J in range(step_count):
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            

        
    elif(x1<-200):
        print("c active")
        GPIO.output(DIR, CCW)
        for J in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
    else:
        GPIO.output(STEP, GPIO.LOW)
                
    if(y1<-200):
        print("P active")
        GPIO.output(DIR1, CCW)
        
        for J in range(step_count):
            GPIO.output(STEP1, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP1, GPIO.LOW)
            sleep(delay)
            
    
    elif(y1>200):
        print("d active")
        GPIO.output(DIR1, CW)
        for J in range(step_count):
            GPIO.output(STEP1, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP1, GPIO.LOW)
            sleep(delay)
    else:
        GPIO.output(STEP1, GPIO.LOW)
        
    
