from datetime import datetime
import time

import RPi.GPIO as GPIO

pinPiezo = 21


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

GPIO.output(pinPiezo, GPIO.HIGH)
time.sleep(0.4)
GPIO.output(pinPiezo, GPIO.LOW)

def alarm(day):
    day

    if time.localtime().tm_hour >= wake_up_times[day][0]:
        if time.localtime().tm_hour == wake_up_times[day][0]:
            if time.localtime().tm_min < wake_up_times[day][1]:
                print("Sleeping %s" % (60 * (wake_up_times[day][1] - time.localtime().tm_min)) + " seconds")
                time.sleep(60 * (wake_up_times[day][1] - time.localtime().tm_min))
            else:
                print("Sleeping %s" % (3600 * (23 - time.localtime().tm_hour) + 60 * (60 - time.localtime().tm_min)) + " seconds")
                time.sleep(3600 * (23 - time.localtime().tm_hour) + 60 * (60 - time.localtime().tm_min))
                alarm(datetime.today().weekday())
        else:
            print("Sleeping %s" % (3600 * (23 - time.localtime().tm_hour) + 60 * (60 - time.localtime().tm_min)) + " seconds")
            time.sleep(3600 * (23 - time.localtime().tm_hour) + 60 * (60 - time.localtime().tm_min))
            alarm(datetime.today().weekday())
    else:
        print("Sleeping %s" % (3600 * (wake_up_times[day][0] - time.localtime().tm_hour) + 60 * (wake_up_times[day][1] - time.localtime().tm_min)) + " seconds")
        time.sleep(3600 * (wake_up_times[day][0] - time.localtime().tm_hour) + 60 * (wake_up_times[day][1] - time.localtime().tm_min))

    return 0

def turnInt(string):

    return int(string)

def importWakeUpData(fileName):

    file = open(fileName, "r")
    separatedDays = file.read().split(",")
    separatedMinHour = []

    for i in separatedDays:

        separatedMinHour.append(list(map(turnInt, i.split(":"))))

    return separatedMinHour


wake_up_times = importWakeUpData("wake_up_time.txt")


# print (wake_up_times)

# print (day(datetime.today().weekday()))
# print (time.localtime().tm_hour)
while (True):
        alarm(datetime.today().weekday())
        while (True):
            GPIO.output(pinPiezo, GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(pinPiezo, GPIO.LOW)
            time.sleep(0.2)