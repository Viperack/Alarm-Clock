from datetime import datetime
import RPi.GPIO as GPIO

pinPiezo = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

GPIO.output(pinPiezo, GPIO.LOW)

def day(dayOfWeek):
    return {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }[dayOfWeek]

#print (day(datetime.today().weekday()))