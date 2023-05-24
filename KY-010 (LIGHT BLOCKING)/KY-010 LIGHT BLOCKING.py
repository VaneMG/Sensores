import machine
import utime

# Configura el pin del sensor
sensor_pin = machine.Pin(17, machine.Pin.IN)

while True:
    # Lee el valor del sensor
    sensor_value = sensor_pin.value()

    if sensor_value == 0:
        print("Luz bloqueada")
    else:
        print("Luz presente")

    utime.sleep(0.1)  # Espera 100 milisegundos antes de leer nuevamente
