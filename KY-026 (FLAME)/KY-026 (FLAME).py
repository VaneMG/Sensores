from machine import Pin#pin lib
import time#time lib

flame = Pin(0,Pin.IN)#analog input
   
while True:#loop 
   if flame.value() == 0:#en analog input, el valor default es 1, al detectar fuego se vuelve 0
       print("fuego!")#alerta en terminal
       time.sleep(1)#sleep de 1 segundo para no saturar la terminal