from machine import Pin
from time import sleep

clk_pin = Pin(16, Pin.IN)
dt_pin = Pin(17, Pin.IN)
sw_pin = Pin(18, Pin.IN)

counter = 0
clk_last = clk_pin.value()

while True:
    clk_current = clk_pin.value()
    dt_current = dt_pin.value()
    sw_current = sw_pin.value()

    if clk_current != clk_last:
        if dt_current != clk_current:
            counter += 1
        else:
            counter -= 1

        print("Counter:", counter)

    clk_last = clk_current

    if sw_current == 0:
        print("Switch pressed")

    sleep(0.01)
