import time
from machine import Pin

led = Pin(26, Pin.OUT)

while True:
   
   print("LED Encendido")
   led.on()  
   time.sleep(5)
   
   print("LED Apagado")
   led.off()    
   time.sleep(5)