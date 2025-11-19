from machine import Pin
from hcsr04 import HCSR04
from time import sleep

#Initialisation du capteur
sensor= HCSR04(trigger_pin=5,echo_pin=18,echo_timeout_us=1000000)

#LEDs
LED_RED=Pin(14,Pin.OUT)
LED_YELLOW=Pin(27,Pin.OUT)
LED_GREEN=Pin(26,Pin.OUT)

#Buzzer
BUZZER=Pin(12,Pin.OUT)

while True:
    distance= sensor.distance_cm()
    print('Distance: %.1f cm' % distance)
    if distance <15 :
        LED_RED.on()
        LED_YELLOW.off()
        LED_GREEN.off()
        BUZZER.on()
        sleep(1)
        
    elif 15 <= distance <= 30:
        LED_RED.off()
        LED_YELLOW.on()
        LED_GREEN.off()
        BUZZER.on()
        sleep(0.1)
        BUZZER.off()
    else:
        LED_RED.off()
        LED_YELLOW.off()
        LED_GREEN.on()
        BUZZER.off()
        sleep(1)
sleep(1)
        
        