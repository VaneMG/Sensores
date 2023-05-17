from machine import Pin
import utime

pin=16
sensor=Pin(pin, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Switch Apagado")
        utime.sleep(1)    
    else:
        print("Switch Encendido")
        utime.sleep(1)
utime.sleep(1)