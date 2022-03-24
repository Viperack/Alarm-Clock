from datetime import datetime
import RPi.GPIO as GPIO

pinPiezo = 40

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

GPIO.output(pinPiezo, 1)

def day(dayOfWeek):
    match dayOfWeek:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case _:        
            return "Incorrect day"

print (day(datetime.today().weekday()))
