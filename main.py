#By: Theodor Köhler
#Date: 2022-06-01

from datetime import datetime #Import av nödvändliga biblotek
import time
import RPi.GPIO as GPIO

pinBuzzer = 21 #Definierar diverse konstanter
pinButton = 20
pinMotionDetector = 16
buttonPressed = False

GPIO.setwarnings(False) #Förbereder läsning och utskick för pinsen
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBuzzer, GPIO.OUT)
GPIO.setup(pinButton, GPIO.IN)
GPIO.setup(pinMotionDetector, GPIO.IN)

GPIO.output(pinBuzzer, GPIO.HIGH) #Test för att kontrollera att programmet körs igång som det ska
time.sleep(0.4)
GPIO.output(pinBuzzer, GPIO.LOW)

# Beskrivning:							Funktionen räknar ut antalet sekunder som är kvar till nästa gång larmet ska aktiveras och pasuar körningen av programmet det antalet sekunder.
# Argument 1:                   		Int - Indikerar vilken dag i vekan det är.
# Return:                   			Int - Return används inte till något.

def alarm(day):
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

# Beskrivning:							Funktionen tar in en sträng och konverterar den till integer.
# Argument 1:                   		String - Strängen som ska konverteras till integer.
# Return:                   			Int - Integers som konverteras från sträng.
# Exempel:								Exempel på olika argument och förväntad return
# "123" => 123
# "" => ValueError
# "a" => ValueError
# "1a" => ValueError

def turnInt(string):
    return int(string)

# Beskrivning:							Funktionen läser in uppväckningsitderna från en .txt fil och formaterar dem i en array
# Argument 1:                   		String - Namnet på filen
# Return:                   			Array - Array där varje element är en array med två integers. Varje element i den yttersta arrayen representerar en dag.

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


# Beskrivning:							Funktionen pausar körningen av programmet i 3 minuter när den kallas på
# Return:                   			Int - Return används inte till något.

def snooze():
    GPIO.output(pinBuzzer, GPIO.LOW)
    print("Snoozed 180 seconds")
    time.sleep(180)
    
    return 0

# Beskrivning:							Funktionen ändrar booleanen buttonPressed till True
# Return:                   			Int - Return används inte till något.

def turnOff(channel):
    global buttonPressed
    buttonPressed = True
    print("Alarm deactivated")
    
    return 0

try:
    wake_up_times = importWakeUpData("wake_up_time.txt")

    while (True):
        alarm(datetime.today().weekday())
        GPIO.add_event_detect(pinButton, GPIO.RISING, callback=turnOff) #Används för att kunna kontrollera om en knapp blir aktiverad samtidigt som programmet är pausas, så kallad asynchronous code.
        while (True):
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
        GPIO.output(pinBuzzer, GPIO.LOW)
        buttonPressed = False
        

except KeyboardInterrupt: #Används för att applikationen ska kunnas avslutas i konsolen
    print("Terminating")
GPIO.cleanup()
    