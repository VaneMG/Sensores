# Dueñas Nuñez Alan Gabriel 19211630
# Código para sensor KY-002 (SHOCK)

import time
from machine import Pin

shock = Pin(0, Pin.IN)
led = Pin("LED", Pin.OUT)

while True:
    
    if shock.value() == 1:
        led.on()
        print("Se detecto una vibración")
        time.sleep(0.1)
        led.off()  