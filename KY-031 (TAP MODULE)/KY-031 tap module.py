import machine
import time

# Configuración de los pines GPIO
tap_pin = machine.Pin(17, machine.Pin.IN)

def tap_detected(pin):
    print("¡Se detectó un golpe!")

# Configuración de interrupción por cambio de estado
tap_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=tap_detected)

while True:
    time.sleep(0.1)
