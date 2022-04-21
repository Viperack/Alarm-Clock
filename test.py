from datetime import datetime
import time
import RPi.GPIO as GPIO

pinBuzzer = 21
pinButton = 20
pinMotionDetector = 16
buttonPressed = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBuzzer, GPIO.OUT)
GPIO.setup(pinButton, GPIO.IN)
GPIO.setup(pinMotionDetector, GPIO.IN)

def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
    GPIO.output(pinBuzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(pinBuzzer, GPIO.LOW)
 
def test(channel):
    print("Test")
        
    return 0

GPIO.add_event_detect(pinButton, GPIO.RISING, callback=test)
 
try:
    #while True:
        #print(GPIO.input(pinMotionDetector))
        #time.sleep(100)
        #if (GPIO.input(pinMotionDetector)):
        #            print("Motion")
        #print(GPIO.input(pinMotionDetector))
    time.sleep(7)
    print("Turned of button")
    GPIO.remove_event_detect(pinButton)
    GPIO.remove_event_detect(pinButton)
except KeyboardInterrupt:
    print("Finish...")
GPIO.cleanup()
