import machine
import time

# Configuración de los pines GPIO
ball_switch_pin = machine.Pin(17, machine.Pin.IN)

while True:
    if ball_switch_pin.value() == 0:
        print("¡El interruptor de la bola está activado!")
    else:
        print("El interruptor de la bola está desactivado.")
    
    time.sleep(0.1)
