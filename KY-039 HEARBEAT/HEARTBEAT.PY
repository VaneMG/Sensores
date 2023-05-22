from machine import Pin, ADC
import utime

POT_Value = ADC(26)
led = Pin("LED", Pin.OUT)
readings = []

print("KY-039 Heartbeat")
print("Coloque el dedo en el sensor\n")

while True:
   
   readings.clear()
   
   while len(readings) <= 5:       
       readings.append(POT_Value.read_u16())
       utime.sleep_ms(20)
   
   average = (sum(readings)/len(readings))/600
   
   if average > 90:
       print(average)
       led.on()
   
   utime.sleep_ms(200)   
   led.off()