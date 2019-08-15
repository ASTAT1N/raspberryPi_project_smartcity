import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)

while True:
    #켜기
    GPIO.output(6, GPIO.HIGH)
    
    #시간 제어
    time.sleep(1)

    #끄기
    GPIO.output(6, GPIO.LOW)
