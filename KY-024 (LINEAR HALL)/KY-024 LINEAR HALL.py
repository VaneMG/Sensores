from machine import Pin
from time import sleep

hall_pin = Pin(16, Pin.IN)

while True:
    value = hall_pin.value()
    print(value)
    sleep(0.1)
