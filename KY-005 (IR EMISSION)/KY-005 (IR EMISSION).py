import machine
import utime

# Define el número de pin utilizado para la señal (S) del KY-005
ir_emitter_pin = machine.Pin(0, machine.Pin.OUT)

# Define el número de pin utilizado para el LED
led_pin = machine.Pin(1, machine.Pin.OUT)

while True:
    # Enciende el emisor de infrarrojos
    ir_emitter_pin.on()
    
    # Enciende el LED
    led_pin.on()
    
    utime.sleep(1)  # Espera 1 segundo
    
    # Apaga el emisor de infrarrojos
    ir_emitter_pin.off()
    
    # Apaga el LED
    led_pin.off()
    
    utime.sleep(1)  # Espera 1 segundo

