from machine import Pin
import time

led_pins = [14,15]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.2
while True:
    for led in leds:
        led.high()
        time.sleep(delay_t)
        led.low()
        time.sleep(delay_t)