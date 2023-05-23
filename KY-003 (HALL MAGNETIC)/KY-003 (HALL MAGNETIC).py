from machine import Pin
import time

iman=Pin(26,Pin.IN)

while True:
    if iman.value() == 0:
        print("Campo detectado")
    elif iman.value()==1:
        print("No se detecta un campo")
    time.sleep(1)