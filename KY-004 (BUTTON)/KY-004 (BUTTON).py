from machine import Pin
from time import sleep

button_pin = Pin(16, Pin.IN)

while True:
    button_state = button_pin.value()

    if button_state == 0:
        print("Button pressed")

    sleep(0.1)