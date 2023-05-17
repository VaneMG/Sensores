from machine import Pin, ADC
from time import sleep

buzzer = Pin(16, Pin.OUT, value=0)

sensor = ADC(0)

while True:
    value = sensor.read_u16()
    print(value)
    sleep(0.5)