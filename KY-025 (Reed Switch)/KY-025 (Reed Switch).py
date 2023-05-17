from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("Hay campo magnetico")
    else:
        print("No hay campo magnetico")
    time.sleep(0.1)