import machine
import time
 
# Configuración del pin de entrada de datos del KY-028
sensor_pin = machine.ADC(26)
 
# Función para convertir la lectura del sensor en grados Celsius
def convert_to_celsius(reading):
    millivolts = (reading * 3300) / 65535
    celsius = (millivolts - 300) / 10
    if celsius < -40:
        celsius = -40
    elif celsius > 125:
        celsius = 125
    return celsius
 
# Bucle principal para leer la temperatura cada segundo
while True:
    # Leer el valor del sensor y convertirlo a grados Celsius
    reading = sensor_pin.read_u16()
    celsius = convert_to_celsius(reading)
 
    # Imprimir la temperatura en la consola
    print("Temperatura actual: {:.2f} C".format(celsius))
 
    # Esperar un segundo antes de volver a leer la temperatura
    time.sleep(1)