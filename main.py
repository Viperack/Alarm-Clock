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

GPIO.output(pinBuzzer, GPIO.HIGH)
time.sleep(0.4)
GPIO.output(pinBuzzer, GPIO.LOW)

def alarm(day):
    if 
    
    if time.localtime().tm_hour >= wake_up_times[day][0]:
        if time.localtime().tm_hour == wake_up_times[day][0]:
            if time.localtime().tm_min < wake_up_times[day][1]:
                seconds = 60 * (wake_up_times[day][1] - time.localtime().tm_min - 1) + 60 - time.localtime().tm_sec
                print("Sleeping %s" % seconds + " seconds")
                time.sleep(seconds)
            else:
                seconds = 3600 * (23 - time.localtime().tm_hour) + 60 * (59 - time.localtime().tm_min) + 60 - time.localtime().tm_sec
                print("Sleeping %s" % seconds + " seconds to next day")
                time.sleep(seconds)
                alarm(datetime.today().weekday())
        else:
            seconds = 3600 * (23 - time.localtime().tm_hour) + 60 * (59 - time.localtime().tm_min) + 60 - time.localtime().tm_sec
            print("Sleeping %s" % seconds + " seconds to next day")
            time.sleep(seconds)
            alarm(datetime.today().weekday())
    else:
        seconds = 3600 * (wake_up_times[day][0] - time.localtime().tm_hour) + 60 * (wake_up_times[day][1] - time.localtime().tm_min - 1) + 60 - time.localtime().tm_sec
        print("Sleeping %s" % seconds + " seconds")
        time.sleep(seconds)

    return 0

def turnInt(string):
    return int(string)

def importWakeUpData(fileName):
    file = open(fileName, "r")
    separatedDays = file.read().split(",")
    separatedMinHour = []

    for i in separatedDays:

        if i == "X":
            separatedMinHour.append("X")
        else:
            separatedMinHour.append(list(map(turnInt, i.split(":"))))

    return separatedMinHour

def snooze():
    GPIO.output(pinBuzzer, GPIO.LOW)
    print("Snoozed 180 seconds")
    time.sleep(180)
    
    return 0

def turnOff(channel):
    global buttonPressed
    buttonPressed = True
    print("Alarm deactivated")
    
    return 0

try:
    wake_up_times = importWakeUpData("wake_up_time.txt")

    while (True):
        alarm(datetime.today().weekday())
        GPIO.add_event_detect(pinButton, GPIO.RISING, callback=turnOff)
        print("T")
        while (True):
            print(buttonPressed)
            GPIO.output(pinBuzzer, GPIO.HIGH)
            for i in range(20):
                if (GPIO.input(pinMotionDetector)):
                    snooze()
                if (buttonPressed):
                    GPIO.remove_event_detect(pinButton)
                    break
                time.sleep(0.02)
            if (buttonPressed):
                    GPIO.remove_event_detect(pinButton)
                    break 
            GPIO.output(pinBuzzer, GPIO.LOW)
            for i in range(10):
                if (GPIO.input(pinMotionDetector)):
                    snooze()        
                if (buttonPressed):
                    GPIO.remove_event_detect(pinButton)
                    break
                time.sleep(0.02)
            if (buttonPressed):
                GPIO.remove_event_detect(pinButton)
                break
        buttonPressed = False
        

except KeyboardInterrupt:
    print("Terminating")
GPIO.cleanup()
    