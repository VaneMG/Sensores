# Sensores

Depto de Sistemas y Computación

Ing. En Sistemas Computacionales

Sistemas Programables 23a

Autor (es):

- Ernesto Gerardo Manuel Aparicio - 18210497
- Alejandro Martinez Reyes - 20210593
- Arturo Rodriguez Jimenez - 20210625
- Carlos Ivan Oroz Quiroz - 17212168
- Arely Vanessa Millán Guízar - 20210599

Repositorio: Sensores



### 1. DS18B20 

Descripción: El sensor de temperatura DS18B20 es uno de los sensores más versátiles que puedes encontrar en el mercado.

Este sensor es idóneo cuando queremos medir la temperatura en ambientes húmedos e incluso dentro del agua.



``` Python
import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(500)
    for rom in roms:
        print(ds_sensor.read_temp(rom))
    time.sleep(1)
```

### 2. KY-002 (SHOCK)

Descripción: El sensor de choque KY-002 es un componente electrónico utilizado para detectar golpes o vibraciones. Consiste en un martillo metálico unido a un mecanismo de resorte y un interruptor que contacta con el martillo. Cuando el martillo se mueve por golpes o vibraciones, presiona el interruptor y cierra el circuito.
El sensor de choque KY-002 es una herramienta útil en muchos proyectos electrónicos donde la detección de golpes o vibraciones es importante. Se puede utilizar, por ejemplo, para activar una alarma cuando se produce un robo o cuando se cae un objeto. También se puede utilizar para monitorear el movimiento de máquinas o dispositivos y controlar su funcionamiento.



``` Python
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
```

### 3. KY-003 (HALL MAGNETIC)

Descripción: El módulo de sensor magnético Hall KY-003 es un interruptor que reacciona a la presencia de un campo magnético, encendiéndose o apagándose. Compatible con microcontroladores populares como Arduino, Raspberry Pi y ESP32.

Este módulo ofrece una salida digital, se parece al sensor magnético hall analógico KY-035, y es funcionalmente similar al KY-024, un sensor magnético digital / analógico.



``` Python
from machine import Pin
import time

iman=Pin(26,Pin.IN)

while True:
    if iman.value() == 0:
        print("Campo detectado")
    elif iman.value()==1:
        print("No se detecta un campo")
    time.sleep(1)
```


### 4. KY-004 (BUTTON)

Descripción: El Módulo ky-004 Sensor Push Button detecta una acción al momento de presionarlo, se utiliza para proyectos en donde se necesite una señal externa.

El Módulo ky-004 Sensor Push Button se utilizan en dispositivos mecánicos y/o electrónicos  para mandar una señal, interruptor o reiniciar un programa.



``` Python
from machine import Pin
from time import sleep

btn = Pin(10,Pin.IN,Pin.PULL_UP)

while True:
    if btn.value()== 0:
        print(a)
 ```
 
### 5. KY-005 (IR EMISSION)

Descripción: El Sensor Infrarrojo Emisor es un módulo KY-005 también llamado diodo emisor infrarrojo es un modulo que convierte la energía eléctrica en luz infrarroja a una frecuencia de 38KHz y una longitud de onda de 940 nm esto se encuentra fuera del espectro detectable por humanos. Consiste en un led IR de 5mm funciona generalmente en conjunto con el receptor de infrarrojo KY-022.



``` Python
#KY-005 IR Emission

import machine
from ir_tx import NEC
import utime

sensorIR = machine.Pin(26, machine.Pin.OUT) #ADC0 sera mi salida de datos analogicos
sensorIR.value(0)# asignamos valor
nec = NEC(sensorIR)
sw = machine.Pin(0,machine.Pin.IN)

while True:
    if sw.value() == 0:
        nec.transmit(0x0000, 0x09) #trasfiero este valor
    machine.sleep_ms(100)
```

### 6. Passive Buzzer

Descripción: Los zumbadores pasivos necesitan una señal de CA para producir sonido. la desventaja de esto es que necesitarán circuitos más complejos para controlarlos, como un temporizador oscilante 555 o un microcontrolador programable como el Arduino.

Los zumbadores pasivos tienen la ventaja de que pueden variar el tono o el tono del sonido. Los zumbadores pasivos se pueden programar para emitir una amplia gama de frecuencias o notas musicales.



``` Python
from machine import Pin, PWM
from time import sleep
buzzer = PWM(Pin(21))

buzzer.duty_u16(1000)

buzzer.freq(523)#DO
sleep(0.5)
buzzer.freq(586)#RE
sleep(0.5)
buzzer.freq(658)#MI
sleep(0.5)
buzzer.freq(697)#FA
sleep(0.5)
buzzer.freq(783)#SO
sleep(0.5)
buzzer.freq(879)#LA
sleep(0.5)
buzzer.freq(987)#SI
sleep(0.5)
buzzer.duty_u16(0)
```

### 7. KY-008 (LASER EMIT)

Descripción: El sensor KY-008 (Laser Emit) es un módulo electrónico que incluye un diodo láser. Este módulo se utiliza principalmente como un componente de salida para emitir un haz de luz láser.



``` Python
import time
from machine import Pin

laser = Pin(26, Pin.OUT)

while True:
    
    print("Laser Encendido")
    laser.on()  
    time.sleep(2)
    
    print("Laser Apagado")
    laser.off()    
    time.sleep(2)
```    

### 8. SMD RBGB

Descripción: Es un diodo emisor de luz de tecnología de montaje superficial. Se caracteriza por tener un encapsulado que permite ser soldado directamente sobre las superficies de las placas de circuitos impresos.



 ``` Python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from picozero import RGBLED
import utime
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import utime

WIDTH  = 128                                         
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
rgb = RGBLED(red=16,green=18,blue=20)
dtpin = Pin(14,Pin.IN,Pin.PULL_UP)
clpin = Pin(15,Pin.IN,Pin.PULL_UP)
rbtn = Pin(13,Pin.IN,Pin.PULL_UP)

value = True
pvalue = False
rvalue = 0
gvalue = 0
bvalue = 0
cycle = "r"
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
writeuwu = Write(oled, ubuntu_mono_20)
def rotary_changed():
    oled.fill(0)
    global pvalue
    global value
    global rvalue,gvalue,bvalue
    global cycle
    if rvalue < 0:
        rvalue = 0
    elif rvalue > 255:
        rvalue == 255
    if gvalue < 0:
        gvalue = 0
    elif gvalue > 255:
        gvalue == 255
    if bvalue < 0:
        bvalue = 0
    elif bvalue > 255:
        bvalue == 255
    if pvalue != clpin.value():
        if clpin.value() == False:
            if dtpin.value() == False:
                if cycle == "r":
                    if rvalue < 255:
                       rvalue = rvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "g":
                    if gvalue < 255:
                       gvalue = gvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "b":
                    if bvalue < 255:
                       bvalue = bvalue + 5
                    else:
                        print("already 255!")
                        
                rgb.color = (rvalue,gvalue,bvalue)
            else:
                if cycle == "r":
                    if rvalue > 0:
                       rvalue = rvalue - 5
                    else:
                        print("already 0!")
                        
                elif cycle == "g":
                    if gvalue > 0:
                       gvalue = gvalue - 5
                    else:
                        print("already 0!")
                elif cycle == "b":
                    if bvalue > 0:
                       bvalue = bvalue - 5
                    else:
                        print("already 0!")
                rgb.color = (rvalue,gvalue,bvalue)
        pvalue = clpin.value()
        writeuwu.text("Red: ", 20, 0)
        writeuwu.text("Green: ", 0, 20)
        writeuwu.text("Blue: ", 10, 40)
        
        writeuwu.text(str(rvalue),60,0)
        writeuwu.text(str(gvalue),60,20)
        writeuwu.text(str(bvalue),60,40)
        oled.show()
    if rbtn.value() == 0:       
        if cycle == "r":
            cycle = "g"
        elif cycle == "g":
            cycle = "b"
        elif cycle == "b":
            cycle = "r"
        utime.sleep(1)
        

while True:
   rotary_changed()
```

### 9. LIGHT BLOCKING

Descripción: El sensor de bloqueo de luz, también conocido como sensor de interrupción de luz, es un tipo de sensor óptico que detecta cambios en la intensidad de la luz al bloquearse o interrumpirse el paso de la luz entre el emisor y el receptor del sensor.



 ``` Python
 
 ```
 
 ### 10. KY-011 (Two-Color)

Descripción: El sensor KY-011 (Two-Color) es un módulo electrónico que combina dos LED de diferentes colores en un solo dispositivo. Este módulo se utiliza para detectar la presencia de luz o para realizar mediciones de color básicas.

El sensor KY-011 consta de dos LED, uno de color rojo y otro de color verde, montados en una pequeña placa de circuito impreso. Cada LED puede encenderse y apagarse de forma independiente.



 ``` Python
 from machine import Pin
import time

led_pins = [16,17]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.1
while True:
    for led in leds:
        led.high()
        time.sleep(delay_t)
        led.low()
        time.sleep(delay_t)
 ```
 
 ### 11. KY-012 (BUZZER)

Descripción: El Sensor Zumbador Activo KY-012 es un dispositivo electrónico que permite reproducir un sonido de un solo tono; a diferencia del KY-006 que puede reproducir diferentes tonos.

El modulo KY-012 integra un zumbador activo, este incorpora un oscilador simple por lo que únicamente es necesario suministrar corriente al dispositivo para que emita sonido. La diferencia de un buzzer activo a un pasivo es que el pasivo necesita recibir una onda de frecuencia.



 ``` Python
 from machine import Pin
from buzzer_music import music
from ssd1306 import SSD1306_I2C
from time import sleep

#tetris, nggyu, pokemon, jingle bells, swth, tloz gff, nokia e
#song = '0 E3 1 0;2 E4 1 0;4 E3 1 0;6 E4 1 0;8 E3 1 0;10 E4 1 0;12 E3 1 0;14 E4 1 0;16 A3 1 0;18 A4 1 0;20 A3 1 0;22 A4 1 0;24 A3 1 0;26 A4 1 0;28 A3 1 0;30 A4 1 0;32 G#3 1 0;34 G#4 1 0;36 G#3 1 0;38 G#4 1 0;40 E3 1 0;42 E4 1 0;44 E3 1 0;46 E4 1 0;48 A3 1 0;50 A4 1 0;52 A3 1 0;54 A4 1 0;56 A3 1 0;58 B3 1 0;60 C4 1 0;62 D4 1 0;64 D3 1 0;66 D4 1 0;68 D3 1 0;70 D4 1 0;72 D3 1 0;74 D4 1 0;76 D3 1 0;78 D4 1 0;80 C3 1 0;82 C4 1 0;84 C3 1 0;86 C4 1 0;88 C3 1 0;90 C4 1 0;92 C3 1 0;94 C4 1 0;96 G2 1 0;98 G3 1 0;100 G2 1 0;102 G3 1 0;104 E3 1 0;106 E4 1 0;108 E3 1 0;110 E4 1 0;114 A4 1 0;112 A3 1 0;116 A3 1 0;118 A4 1 0;120 A3 1 0;122 A4 1 0;124 A3 1 0;0 E6 1 1;4 B5 1 1;6 C6 1 1;8 D6 1 1;10 E6 1 1;11 D6 1 1;12 C6 1 1;14 B5 1 1;0 E5 1 6;4 B4 1 6;6 C5 1 6;8 D5 1 6;10 E5 1 6;11 D5 1 6;12 C5 1 6;14 B4 1 6;16 A5 1 1;20 A5 1 1;22 C6 1 1;24 E6 1 1;28 D6 1 1;30 C6 1 1;32 B5 1 1;36 B5 1 1;36 B5 1 1;37 B5 1 1;38 C6 1 1;40 D6 1 1;44 E6 1 1;48 C6 1 1;52 A5 1 1;56 A5 1 1;20 A4 1 6;16 A4 1 6;22 C5 1 6;24 E5 1 6;28 D5 1 6;30 C5 1 6;32 B4 1 6;36 B4 1 6;37 B4 1 6;38 C5 1 6;40 D5 1 6;44 E5 1 6;48 C5 1 6;52 A4 1 6;56 A4 1 6;64 D5 1 6;64 D6 1 1;68 D6 1 1;70 F6 1 1;72 A6 1 1;76 G6 1 1;78 F6 1 1;80 E6 1 1;84 E6 1 1;86 C6 1 1;88 E6 1 1;92 D6 1 1;94 C6 1 1;96 B5 1 1;100 B5 1 1;101 B5 1 1;102 C6 1 1;104 D6 1 1;108 E6 1 1;112 C6 1 1;116 A5 1 1;120 A5 1 1;72 A5 1 6;80 E5 1 6;68 D5 1 7;70 F5 1 7;76 G5 1 7;84 E5 1 7;78 F5 1 7;86 C5 1 7;88 E5 1 6;96 B4 1 6;104 D5 1 6;112 C5 1 6;120 A4 1 6;92 D5 1 7;94 C5 1 7;100 B4 1 7;101 B4 1 7;102 C5 1 7;108 E5 1 7;116 A4 1 7'
#song = '0 F#5 1 0;0 A#5 1 0;0 C#6 1 0;6 D#6 1 0;6 C6 1 0;6 G#5 1 0;12 G#5 1 0;16 D#6 1 0;16 C6 1 0;16 G#5 1 0;22 F6 1 0;22 A#5 1 0;22 C#6 1 0;28 G#6 1 0;29 F#6 1 0;30 F6 1 0;31 D#6 1 0;0 F#4 1 0;0 A#4 1 0;0 C#5 1 0;6 D#5 1 0;6 C5 1 0;6 G#4 1 0;12 G#4 1 0;16 D#5 1 0;16 C5 1 0;16 G#4 1 0;22 F5 1 0;22 A#4 1 0;22 C#5 1 0;28 G#5 1 0;29 F#5 1 0;30 F5 1 0;31 D#5 1 0;32 F#5 1 0;32 A#5 1 0;32 C#6 1 0;38 D#6 1 0;38 C6 1 0;38 G#5 1 0;44 G#5 1 0;32 F#4 1 0;32 A#4 1 0;32 C#5 1 0;38 D#5 1 0;38 C5 1 0;38 G#4 1 0;44 G#4 1 0;58 G#4 1 0;59 G#4 1 0;60 A#4 1 0;61 C#5 1 0;62 A#4 1 0;63 C#5 1 0;0 F#4 1 6;0 A#4 1 6;0 C#5 1 6;6 D#5 1 6;6 C5 1 6;6 G#4 1 6;12 G#4 1 6;16 D#5 1 6;16 C5 1 6;16 G#4 1 6;22 F5 1 6;22 A#4 1 6;22 C#5 1 6;28 G#5 1 6;29 F#5 1 6;30 F5 1 6;31 D#5 1 6;0 F#3 1 6;0 A#3 1 6;0 C#4 1 6;6 D#4 1 6;6 C4 1 6;6 G#3 1 6;12 G#3 1 6;16 D#4 1 6;16 C4 1 6;16 G#3 1 6;22 F4 1 6;22 A#3 1 6;22 C#4 1 6;28 G#4 1 6;29 F#4 1 6;30 F4 1 6;31 D#4 1 6;32 F#4 1 6;32 A#4 1 6;32 C#5 1 6;38 D#5 1 6;38 C5 1 6;38 G#4 1 6;44 G#4 1 6;32 F#3 1 6;32 A#3 1 6;32 C#4 1 6;38 D#4 1 6;38 C4 1 6;38 G#3 1 6;44 G#3 1 6;58 G#3 1 6;59 G#3 1 6;60 A#3 1 6;61 C#4 1 6;62 A#3 1 6;63 C#4 1 6;0 F#2 1 29;2 F#2 1 29;4 F#2 1 29;6 G#2 1 29;8 G#2 1 29;10 G#2 1 29;12 G#2 1 29;13 G#2 1 29;14 G#2 1 29;15 G#2 1 29;16 G#2 1 29;18 G#2 1 29;20 G#2 1 29;22 A#2 1 29;24 A#2 1 29;26 A#2 1 29;28 A#2 1 29;29 A#2 1 29;30 A#2 1 29;31 A#2 1 29;32 F#2 1 29;34 F#2 1 29;36 F#2 1 29;38 G#2 1 29;40 G#2 1 29;42 G#2 1 29;44 G#2 1 29;45 G#2 1 29;46 G#2 1 29;47 G#2 1 29;48 G#2 1 29;50 G#2 1 29;52 G#2 1 29;54 A#2 1 29;56 A#2 1 29;58 A#2 1 29;60 A#2 1 29;61 A#2 1 29;62 A#2 1 29;63 A#2 1 29;0 C3 1 2;2 D#3 1 2;4 C3 1 2;6 D#3 1 2;3 D#3 1 2;2 F#3 1 2;3 F#3 1 2;6 F#3 1 2;0 B2 1 2;4 B2 1 2;8 C3 1 2;8 B2 1 2;10 D#3 1 2;11 D#3 1 2;10 F#3 1 2;11 F#3 1 2;14 F#3 1 2;14 D#3 1 2;12 C3 1 2;12 B2 1 2;16 C3 1 2;18 D#3 1 2;20 C3 1 2;22 D#3 1 2;19 D#3 1 2;18 F#3 1 2;19 F#3 1 2;22 F#3 1 2;16 B2 1 2;20 B2 1 2;24 C3 1 2;24 B2 1 2;26 D#3 1 2;27 D#3 1 2;26 F#3 1 2;27 F#3 1 2;30 F#3 1 2;30 D#3 1 2;28 C3 1 2;28 B2 1 2;32 C3 1 2;34 D#3 1 2;36 C3 1 2;38 D#3 1 2;35 D#3 1 2;34 F#3 1 2;35 F#3 1 2;38 F#3 1 2;32 B2 1 2;36 B2 1 2;40 C3 1 2;40 B2 1 2;42 D#3 1 2;43 D#3 1 2;42 F#3 1 2;43 F#3 1 2;46 F#3 1 2;46 D#3 1 2;44 C3 1 2;44 B2 1 2;48 C3 1 2;50 D#3 1 2;52 C3 1 2;54 D#3 1 2;51 D#3 1 2;50 F#3 1 2;51 F#3 1 2;54 F#3 1 2;48 B2 1 2;52 B2 1 2;56 C3 1 2;56 B2 1 2;58 D#3 1 2;59 D#3 1 2;58 F#3 1 2;59 F#3 1 2;62 F#3 1 2;62 D#3 1 2;60 C3 1 2;60 B2 1 2;60 D#3 1 2;61 D#3 1 2;63 D#3 1 2;0 G#2 1 2;2 G#2 1 2;3 G#2 1 2;4 G#2 1 2;32 G#2 1 2;34 G#2 1 2;35 G#2 1 2;36 G#2 1 2;0 E2 1 2;2 E2 1 2;4 E2 1 2;6 E2 1 2;8 E2 1 2;10 E2 1 2;12 E2 1 2;14 E2 1 2;15 E2 1 2;16 E2 1 2;18 E2 1 2;20 E2 1 2;22 E2 1 2;24 E2 1 2;26 E2 1 2;28 E2 1 2;30 E2 1 2;31 E2 1 2;32 E2 1 2;34 E2 1 2;36 E2 1 2;38 E2 1 2;40 E2 1 2;42 E2 1 2;44 E2 1 2;46 E2 1 2;47 E2 1 2;48 E2 1 2;50 E2 1 2;52 E2 1 2;54 E2 1 2;56 E2 1 2;58 E2 1 2;60 E2 1 2;62 E2 1 2;63 E2 1 2;0 F#3 1 12;1 A#3 1 12;2 C#4 1 12;3 A#3 1 12;0 C#4 1 12;0 A#3 1 12;4 A#3 1 12;4 F#3 1 12;4 C#4 1 12;5 A#3 1 12;6 G#3 1 12;6 C4 1 12;6 D#4 1 12;7 C4 1 12;8 D#4 1 12;9 C4 1 12;10 G#3 1 12;10 C4 1 12;10 D#4 1 12;11 C4 1 12;13 C4 1 12;14 G#3 1 12;14 C4 1 12;15 C4 1 12;15 G#3 1 12;12 D#4 1 12;14 D#4 1 12;15 D#4 1 12;16 G#3 1 12;17 C4 1 12;18 D#4 1 12;19 C4 1 12;16 D#4 1 12;16 C4 1 12;20 C4 1 12;20 G#3 1 12;20 D#4 1 12;21 C4 1 12;22 A#3 1 12;22 F4 1 12;24 F4 1 12;26 A#3 1 12;26 F4 1 12;30 A#3 1 12;31 A#3 1 12;28 F4 1 12;30 F4 1 12;31 F4 1 12;22 C#4 1 12;23 C#4 1 12;25 C#4 1 12;26 C#4 1 12;27 C#4 1 12;29 C#4 1 12;30 C#4 1 12;31 C#4 1 12;32 F#3 1 12;33 A#3 1 12;34 C#4 1 12;35 A#3 1 12;32 C#4 1 12;32 A#3 1 12;36 A#3 1 12;36 F#3 1 12;36 C#4 1 12;37 A#3 1 12;38 G#3 1 12;38 C4 1 12;38 D#4 1 12;39 C4 1 12;40 D#4 1 12;41 C4 1 12;42 G#3 1 12;42 C4 1 12;42 D#4 1 12;43 C4 1 12;45 C4 1 12;46 G#3 1 12;46 C4 1 12;47 C4 1 12;47 G#3 1 12;44 D#4 1 12;46 D#4 1 12;47 D#4 1 12;48 G#3 1 12;49 C4 1 12;50 D#4 1 12;51 C4 1 12;48 D#4 1 12;48 C4 1 12;52 C4 1 12;52 G#3 1 12;52 D#4 1 12;53 C4 1 12;54 A#3 1 12;54 F4 1 12;56 F4 1 12;58 A#3 1 12;58 F4 1 12;62 A#3 1 12;63 A#3 1 12;60 F4 1 12;62 F4 1 12;63 F4 1 12;54 C#4 1 12;55 C#4 1 12;57 C#4 1 12;58 C#4 1 12;59 C#4 1 12;61 C#4 1 12;62 C#4 1 12;63 C#4 1 12;0 F#5 1 6;0 A#5 1 6;0 C#6 1 6;6 D#6 1 6;6 C6 1 6;6 G#5 1 6;12 G#5 1 6;16 D#6 1 6;16 C6 1 6;16 G#5 1 6;22 F6 1 6;22 A#5 1 6;22 C#6 1 6;28 G#6 1 6;29 F#6 1 6;30 F6 1 6;31 D#6 1 6;0 F#4 1 6;0 A#4 1 6;0 C#5 1 6;6 D#5 1 6;6 C5 1 6;6 G#4 1 6;12 G#4 1 6;16 D#5 1 6;16 C5 1 6;16 G#4 1 6;22 F5 1 6;22 A#4 1 6;22 C#5 1 6;28 G#5 1 6;29 F#5 1 6;30 F5 1 6;31 D#5 1 6;32 F#5 1 6;32 A#5 1 6;32 C#6 1 6;38 D#6 1 6;38 C6 1 6;38 G#5 1 6;44 G#5 1 6;32 F#4 1 6;32 A#4 1 6;32 C#5 1 6;38 D#5 1 6;38 C5 1 6;38 G#4 1 6;44 G#4 1 6;58 G#4 1 6;59 G#4 1 6;60 A#4 1 6;61 C#5 1 6;62 A#4 1 6;63 C#5 1 6;0 C#6 6 23;6 D#6 6 23;12 G#5 4 23;16 D#6 6 23;22 F6 6 23;54 F6 6 23;32 C#6 6 23;38 D#6 6 23;44 G#5 4 23;48 D#6 6 23;48 D#7 6 23;54 F7 6 23;48 G#5 6 9;54 A#5 6 9;0 F#4 6 9;6 G#4 6 9;12 C#4 4 9;16 G#4 6 9;22 A#4 6 9;54 A#4 6 9;32 F#4 6 9;38 G#4 6 9;44 C#4 4 9;48 G#4 6 9;0 F#6 1 20;2 F#6 1 20;4 F#6 1 20;6 G#6 1 20;8 G#6 1 20;10 G#6 1 20;12 G#6 1 20;13 G#6 1 20;14 G#6 1 20;15 G#6 1 20;16 G#6 1 20;18 G#6 1 20;20 G#6 1 20;22 A#6 1 20;24 A#6 1 20;26 A#6 1 20;28 A#6 1 20;29 A#6 1 20;30 A#6 1 20;31 G#6 1 20;32 F#6 1 20;34 F#6 1 20;36 F#6 1 20;38 G#6 1 20;40 G#6 1 20;42 G#6 1 20;44 G#6 1 20;45 G#6 1 20;46 G#6 1 20;47 G#6 1 20;48 G#6 1 20;50 G#6 1 20;52 G#6 1 20;54 A#6 1 20;56 A#6 1 20;58 A#6 1 20;60 A#6 1 20;61 A#6 1 20;62 A#6 1 20;63 G#6 1 20'
#song = '0 D6 2 0;2 D6 2 0;4 A6 4 0;8 D6 2 0;10 D6 2 0;12 A#6 4 0;16 D6 2 0;18 D6 2 0;20 A6 4 0;24 D6 2 0;26 D6 2 0;28 F#6 4 0;32 D6 2 0;34 D6 2 0;36 A6 4 0;40 D6 2 0;42 D6 2 0;44 C#7 4 0;48 D7 8 0;56 D6 8 0;64 C7 8 0;72 C6 8 0;80 D6 2 0;82 D6 2 0;84 A6 4 0;88 D6 2 0;90 D6 2 0;92 A#6 4 0;96 D6 2 0;98 D6 2 0;100 C7 4 0;104 D6 2 0;106 D6 2 0;108 C#7 4 0;112 D7 16 0;128 D7 4 0;138.6699981689453 G5 1 0;140 B5 1 0;141.3300018310547 D6 1 0;142.6699981689453 F#6 1 0;144 G6 4 0;148 G6 4 0;154 G6 1 0;155 G6 1 0;156 G6 4 0;160 G6 4 0;164 G6 4 0;168 F6 1 0;169.3300018310547 F6 1 0;170.6699981689453 F6 1 0;172 F6 1 0;173.3300018310547 F6 1 0;174.6699981689453 F#6 1 0;176 G6 6 0;182 B6 2 0;184 D7 8 0;192 C6 6 0;198 F6 2 0;200 F7 6 0;206 E7 1 0;207 D#7 1 0;208 D7 8 0;216 F6 6 0;222 E6 1 0;223 D#6 1 0;224 D6 8 0;232 C6 3 0;234.6699981689453 B5 3 0;237.3300018310547 C6 3 0;240 G6 6 0;246 B6 2 0;248 D7 8 0;256 C6 8 0;264 C7 3 0;266.6700134277344 B6 3 0;269.3299865722656 C7 3 0;272 D7 8 0;280 F6 3 0;282.6700134277344 E6 3 0;285.3299865722656 C6 3 0;288 D6 8 0;298 B5 2 0;300 C6 2 0;302 D6 2 0;304 G6 6 0;310 B6 2 0;312 D7 8 0;320 C6 6 0;326 F6 2 0;328 F7 6 0;334 E7 1 0;335 D#7 1 0;336 D7 8 0;344 F6 6 0;350 E6 1 0;351 D#6 1 0;352 D6 8 0;360 C6 3 0;362.6700134277344 B5 3 0;365.3299865722656 C6 3 0;368 G6 6 0;374 B6 2 0;376 D7 8 0;384 C6 8 0;392 F7 3 0;394.6700134277344 E7 3 0;397.3299865722656 F7 3 0;400 G7 6 0;406 A#7 2 0;408 G7 16 0;424 A7 8 0;432 A#7 6 0;438 F7 2 0;440 F7 16 0;456 A#7 4 0;460 B7 4 0;464 C7 6 0;470 G7 2 0;480 G6 4 0;484 G6 4 0;472 G7 16 0;488 C7 4 0;492 C#7 4 0;496 D7 2 0;499 D7 1 0;503 D7 1 0;507 D7 1 0;511 D7 1 0;515 D7 1 0;519 D7 1 0;520 C7 3 0;522.6699829101562 C7 3 0;525.3300170898438 C#7 3 0;528 D7 2 0;531 D7 1 0;535 D7 1 0;539 D7 1 0;543 D7 1 0;544 D7 3 0;547 D7 1 0;551 D7 1 0;552 C7 3 0;560 G6 6 0;566 B6 2 0;568 D7 8 0;582 F6 2 0;584 F7 6 0;590 E7 1 0;591 D#7 1 0;592 D7 8 0;600 F6 6 0;606 E6 1 0;607 D#6 1 0;608 D6 8 0;616 C6 3 0;618.6699829101562 B5 3 0;621.3300170898438 C6 3 0;624 G6 6 0;630 B6 2 0;632 D7 8 0;640 C6 8 0;648 C7 3 0;650.6699829101562 B6 3 0;653.3300170898438 C7 3 0;656 D7 8 0;664 F6 3 0;666.6699829101562 E6 3 0;669.3300170898438 C6 3 0;672 D6 8 0;682 B5 2 0;684 C6 2 0;686 D6 2 0;688 G6 6 0;694 B6 2 0;696 D7 8 0;704 C6 6 0;710 F6 2 0;712 F7 6 0;718 E7 1 0;719 D#7 1 0;720 D7 8 0;728 F6 6 0;734 E6 1 0;735 D#6 1 0;736 D6 8 0;744 C6 3 0;746.6699829101562 B5 3 0;749.3300170898438 C6 3 0;752 G6 6 0;758 B6 2 0;760 D7 8 0;768 C6 8 0;776 F7 3 0;778.6699829101562 E7 3 0;781.3300170898438 F7 3 0;784 G7 6 0;790 A#7 2 0;792 G7 16 0;808 A7 8 0;816 A#7 6 0;822 F7 2 0;824 F7 16 0;840 A#7 4 0;844 B7 4 0;848 C7 6 0;854 G7 2 0;856 G7 16 0;872 C7 4 0;876 C#7 4 0;880 D7 2 0;883 D7 1 0;887 D7 1 0;891 D7 1 0;895 D7 1 0;899 D7 1 0;903 D7 1 0;904 C7 3 0;906.6699829101562 C7 3 0;909.3300170898438 C#7 3 0;912 D7 2 0;915 D7 1 0;919 D7 1 0;923 D7 1 0;927 D7 1 0;928 D7 3 0;931 D7 1 0;935 D7 1 0;936 C7 3 0;938.6699829101562 C7 3 0;941.3300170898438 C#7 3 0;944 D7 2 0;947 D7 1 0;951 D7 1 0;955 D7 1 0;959 D7 1 0;963 D7 1 0;967 D7 1 0;968 C7 3 0;970.6699829101562 C7 3 0;973.3300170898438 C#7 3 0;976 D7 2 0;979 D7 1 0;983 D7 1 0;987 D7 1 0;991 D7 1 0;992 D7 3 0;995 D7 1 0;999 D7 1 0;1000 C7 3 0;1003 C7 3 0;555 C7 3 0;558 B6 1 0;1006 B6 1 0;1008 G6 1 0'
#song = '0 G4 1 8;1 E5 1 8;2 D5 1 8;3 C5 1 8;8 G4 1 8;9 E5 1 8;10 D5 1 8;11 C5 1 8;4 G4 3 8;12 A4 4 8;7 G4 0.5 8;7.5 G4 0.5 8;16 A4 1 8;17 F5 1 8;18 E5 1 8;19 D5 1 8;20 B4 4 8;24 G5 1 8;25 G5 1 8;26 F5 1 8;27 D5 1 8;28 E5 4 8;28 C5 4 8;32 G4 1 8;33 E5 1 8;34 D5 1 8;35 C5 1 8;36 G4 4 8;40 G4 1 8;41 E5 1 8;42 D5 1 8;43 C5 1 8;44 A4 3 8;47 A4 1 8;48 A4 1 8;49 F5 1 8;50 E5 1 8;51 D5 1 8;52 G5 1 8;53 G5 1 8;54 G5 1 8;55 G5 1 8;56 A5 1 8;57 G5 1 8;58 F5 1 8;59 D5 1 8;60 C5 1 8;62 G5 2 8;64 E5 1 8;65 E5 1 8;66 E5 2 8;64 G4 1 8;64 C4 1 8;65 G4 1 8;65 C4 1 8;66 G4 2 8;66 C4 2 8;68 E5 1 8;69 E5 1 8;70 E5 2 8;68 G4 1 8;68 C4 1 8;69 G4 1 8;69 C4 1 8;70 G4 2 8;70 C4 2 8;96 E5 1 8;97 E5 1 8;98 E5 2 8;96 G4 1 8;96 C4 1 8;97 G4 1 8;97 C4 1 8;98 G4 2 8;98 C4 2 8;100 E5 1 8;101 E5 1 8;102 E5 2 8;100 G4 1 8;100 C4 1 8;101 G4 1 8;101 C4 1 8;102 G4 2 8;102 C4 2 8;72 E5 1 8;73 G5 1 8;74 C5 1 8;75 D5 1 8;76 C5 4 8;76 E5 4 8;80 F5 1 8;81 F5 1 8;82 F5 1 8;83 F5 1 8;84 F5 1 8;85 E5 1 8;86 E5 1 8;87 E5 1 8;88 E5 1 8;89 D5 1 8;90 D5 1 8;91 E5 1 8;92 D5 2 8;94 G5 2 8;104 E5 1 8;105 G5 1 8;106 C5 1 8;107 D5 1 8;108 C5 4 8;108 E5 4 8;112 F5 1 8;113 F5 1 8;114 F5 1 8;115 F5 1 8;116 F5 1 8;117 E5 1 8;118 E5 1 8;119 E5 1 8;120 G5 1 8;121 G5 1 8;122 F5 1 8;123 D5 1 8;124 C5 2 8;126 C5 1 8;126 G4 1 8;126 E4 1 8;126 C4 1 8;128 G3 4 8;128 D4 4 8;132 D4 4 8;132 G3 4 8;140 D4 4 8;140 G3 4 8;136 D4 2 8;138 D4 2 8;136 G3 2 8;138 G3 2 8;146 G3 2 8;146 D4 2 8;150 G3 2 8;150 D4 2 8;144 D4 1 8;145 D4 1 8;144 G3 1 8;145 G3 1 8;148 D4 1 8;149 D4 1 8;148 G3 1 8;149 G3 1 8;144 B5 1 8;145 B5 1 8;146 B5 2 8;148 B5 1 8;149 B5 1 8;150 B5 2 8;152 B5 1 8;153 D6 1 8;154 G5 1 8;155 A5 1 8;156 G5 4 8;156 B5 4 8;160 C6 1 8;161 C6 1 8;162 C6 1 8;163 C6 1 8;164 C6 1 8;165 B5 1 8;166 B5 1 8;167 B5 1 8;168 B5 1 8;169 A5 1 8;170 A5 1 8;171 B5 1 8;172 A5 2 8;174 D6 2 8;178 B5 2 8;182 B5 2 8;176 B5 1 8;177 B5 1 8;180 B5 1 8;181 B5 1 8;184 B5 1 8;185 D6 1 8;186 G5 1 8;187 A5 1 8;192 C6 1 8;193 C6 1 8;194 C6 1 8;195 C6 1 8;196 C6 1 8;197 B5 1 8;198 B5 1 8;199 B5 1 8;200 D6 1 8;201 D6 1 8;202 C6 1 8;203 A5 1 8;208 D6 1 8;209 D6 1 8;210 C6 1 8;211 A5 1 8;212 G5 2 8;214 G6 1 8;172 D4 4 8;178 G3 2 8;178 D4 2 8;182 G3 2 8;182 D4 2 8;176 D4 1 8;177 D4 1 8;176 G3 1 8;177 G3 1 8;180 D4 1 8;181 D4 1 8;180 G3 1 8;181 G3 1 8;204 D4 1 8;205 D4 1 8;206 C4 1 8;207 B3 1 8;212 G3 3 8;212 D4 3 8;188 B5 4 8;188 G5 4 8'
#song = '0 A4 4 1;2 C5 4 1;4 E5 4 1;6 A5 4 1;8 B5 4 1;8 G#4 4 1;10 E5 4 1;12 C5 4 1;14 B5 4 1;16 C6 4 1;16 G4 4 1;18 E5 4 1;20 C5 4 1;22 C6 4 1;24 F#5 4 1;24 F#4 4 1;26 D5 4 1;28 A4 4 1;30 F#5 4 1;32 E5 4 1;32 F4 4 1;34 C5 4 1;36 A4 4 1;38 C5 4 1;42 E5 4 1;44 C5 4 1;46 A4 4 1;50 A3 4 1;48 B4 4 1;48 G4 4 1;50 C5 4 1;50 A4 4 1;48 B3 4 1;52 C5 4 1;52 A4 4 1;52 A3 4 1;48 G3 4 1;58 A3 4 1;60 F4 4 1;62 E4 4 1;64 A4 4 1;66 C5 4 1;68 E5 4 1;70 A5 4 1;72 B5 4 1;72 G#4 4 1;74 E5 4 1;76 C5 4 1;78 B5 4 1;80 C6 4 1;80 G4 4 1;82 E5 4 1;84 C5 4 1;86 C6 4 1;88 F#5 4 1;88 F#4 4 1;90 D5 4 1;92 A4 4 1;94 F#5 4 1;96 E5 4 1;96 F4 4 1;98 C5 4 1;100 A4 4 1;102 C5 4 1;106 E5 4 1;108 C5 4 1;110 A4 4 1;114 A3 4 1;112 B4 4 1;112 G4 4 1;114 C5 4 1;114 A4 4 1;112 B3 4 1;116 C5 4 1;116 A4 4 1;116 A3 4 1;112 G3 4 1;124 A3 4 1;126 B3 4 1;128 C4 4 1;128 C5 4 1;130 E4 4 1;132 G4 4 1;134 C5 4 1;136 F#5 4 1;136 D4 4 1;138 D5 4 1;140 A4 4 1;140 A4 4 1;142 F#5 4 1;144 E5 4 1;146 C5 4 1;148 A4 4 1;144 F4 4 1;150 E5 4 1;64 E6 4 23;64 C6 4 23;64 E5 4 23;68 E5 4 23;68 C6 4 23;68 E6 4 23;72 E6 6 23;72 C6 6 23;72 E5 6 23;78 E6 2 23;78 C6 2 23;78 E5 2 23;80 A5 4 23;96 C6 4 23;96 A5 4 23;100 C6 12 23;100 A5 12 23;112 D6 2 23;112 B5 2 23;112 G5 2 23;114 E6 2 23;116 E6 12 23;114 C6 2 23;116 C6 12 23;114 A5 2 23;116 A5 12 23;128 E6 4 23;128 C6 4 23;128 G5 4 23;136 F#6 4 23;136 D6 4 23;136 A5 4 23;152 B4 4 1;153 C5 4 1;154 A4 4 1;156 A3 4 1;158 B3 4 1;160 C4 4 1;162 E4 4 1;164 G4 4 1;166 C5 4 1;168 G3 4 1;168 G5 4 1;168 G4 4 1;170 D5 4 1;172 G4 4 1;174 G5 4 1;176 G5 4 1;177 F#5 4 1;176 D4 4 1;192 C4 4 1;192 C5 4 1;194 E4 4 1;196 G4 4 1;198 C5 4 1;200 F#5 4 1;200 D4 4 1;202 D5 4 1;204 A4 4 1;204 A4 4 1;206 F#5 4 1;208 E5 4 1;210 C5 4 1;212 A4 4 1;208 F4 4 1;214 E5 4 1;216 B4 4 1;217 C5 4 1;218 A4 4 1;144 A6 4 23;144 F6 4 23;144 C6 4 23;148 A5 2 23;148 D6 2 23;148 G6 2 23;150 F6 2 23;152 E6 6 23;152 C6 6 23;152 A5 6 23;158 G5 2 23;158 D6 2 23;158 G6 2 23;160 E6 4 23;160 C6 4 23;160 G5 4 23;168 D6 4 23;168 G5 4 23;168 E6 4 23;174 C6 2 23;188 A3 4 1;192 C5 4 1;190 B3 4 1;192 A6 4 23;192 E6 4 23;192 C6 4 23;196 A6 2 23;196 E6 2 23;196 C6 2 23;198 B5 2 23;198 E6 2 23;198 G6 2 23;200 G6 2 23;200 B5 2 23;200 D6 2 23;202 D6 2 23;202 F#6 2 23;202 A5 2 23;204 E6 2 23;204 C6 2 23;204 G5 2 23;206 D6 2 23;206 A5 2 23;206 F#5 2 23;208 A6 2 23;208 E6 2 23;208 C6 2 23;210 A6 2 23;210 E6 2 23;210 C6 2 23;212 D6 2 23;212 C7 2 23;212 E6 2 23;214 B6 2 23;214 C6 2 23;214 G6 2 23;216 E6 4 23;216 C7 4 23;216 A6 4 23;220 D7 4 23;224 E7 4 23;224 G6 4 23;224 C6 4 23;228 E7 4 23;228 G6 4 23;228 C6 4 23;232 D7 4 23;232 F#6 4 23;232 A5 4 23;220 A4 4 1;222 B4 4 1;224 C5 4 1;220 A3 4 1;222 B3 4 1;224 C4 4 1;226 E4 4 1;228 G4 4 1;230 C5 4 1;232 D4 4 1;234 D5 4 1;236 A4 4 1;238 E5 2 1;254 B4 2 32;256 C5 2 32;260 B4 2 32;262 A4 2 32;264 B4 2 32;270 A4 1 32;271 B4 1 32;272 C5 2 32;274 D5 2 32;278 C5 2 32;280 A4 2 32;284 C5 2 32;286 D5 2 32;288 E5 2 32;292 D5 2 32;294 C5 2 32;296 B4 1 32;297 A4 1 32;302 E4 2 32;304 G4 2 32;306 A4 2 32;308 A4 2 32;316 A4 2 32;318 B4 2 32;320 C5 2 32;322 B4 2 32;326 A4 2 32;328 A4 1 32;329 B4 1 32;334 A4 1 32;335 B4 1 32;336 C5 2 32;338 D5 2 32;342 C5 2 32;344 B4 2 32;346 A4 2 32;350 C5 1 32;351 D5 1 32;352 E5 2 32;354 D5 2 32;356 C5 2 32;358 B4 2 32;360 A4 2 32;362 A4 2 32;368 G4 2 32;370 A4 2 32;372 A4 2 32;388 C5 2 32;390 E5 2 32;392 D5 2 32;400 D5 2 32;406 C5 1 32;407 B4 1 32;408 C5 1 32;409 A4 1 32;410 A4 2 32;414 B4 2 32;416 C5 2 32;418 E5 2 32;420 C5 2 32;422 B4 2 32;424 C5 2 32;426 A4 2 32;430 A4 2 32;432 G4 2 32;434 A4 2 32;436 A4 2 32;174 G6 2 23;176 A6 2 23;178 A6 8 23;176 E6 2 23;178 E6 8 23;176 A5 2 23;178 A5 8 23;448 C5 2 32;452 B4 2 32;454 A4 2 32;456 B4 2 32;462 A4 1 32;463 B4 1 32;464 C5 2 32;468 D5 2 32;470 C5 2 32;472 B4 2 32;474 A4 2 32;480 E5 2 32;482 D5 2 32;484 C5 2 32;486 B4 2 32;490 A4 2 32;492 B4 2 32;446 B4 2 32;444 A4 2 32;252 A4 2 32;176 D5 2 1;176 G4 2 1;178 D5 2 1;180 D5 4 1;178 F#5 2 1;180 F#5 4 1;240 E5 2 1;242 E5 2 1;244 E5 2 1;240 C5 2 1;242 C5 2 1;244 C5 2 1;240 A4 2 1;242 A4 2 1;244 A4 2 1;240 F4 2 1;242 F4 2 1;256 A4 4 1;258 C5 4 1;260 E5 4 1;262 A5 4 1;264 B5 4 1;264 G#4 4 1;266 E5 4 1;268 C5 4 1;270 B5 4 1;272 C6 4 1;272 G4 4 1;274 E5 4 1;276 C5 4 1;278 C6 4 1;280 F#5 4 1;280 F#4 4 1;282 D5 4 1;284 A4 4 1;286 F#5 4 1;288 E5 4 1;288 F4 4 1;290 C5 4 1;292 A4 4 1;294 C5 4 1;298 E5 4 1;300 C5 4 1;302 A4 4 1;306 A3 4 1;304 B4 4 1;304 G4 4 1;306 C5 4 1;306 A4 4 1;304 B3 4 1;308 C5 4 1;308 A4 4 1;308 A3 4 1;304 G3 4 1;314 A3 4 1;316 F4 4 1;318 E4 4 1;320 A4 4 1;322 C5 4 1;324 E5 4 1;326 A5 4 1;328 B5 4 1;328 G#4 4 1;330 E5 4 1;332 C5 4 1;334 B5 4 1;336 C6 4 1;336 G4 4 1;338 E5 4 1;340 C5 4 1;342 C6 4 1;344 F#5 4 1;344 F#4 4 1;346 D5 4 1;348 A4 4 1;350 F#5 4 1;352 E5 4 1;352 F4 4 1;354 C5 4 1;356 A4 4 1;358 C5 4 1;362 E5 4 1;364 C5 4 1;366 A4 4 1;370 A3 4 1;368 B4 4 1;368 G4 4 1;370 C5 4 1;370 A4 4 1;368 B3 4 1;372 C5 4 1;372 A4 4 1;372 A3 4 1;368 C3 4 1;380 A3 4 1;382 B3 4 1;384 C4 4 1;384 C5 4 1;386 E4 4 1;388 G4 4 1;390 C5 4 1;392 F#5 4 1;392 D4 4 1;394 D5 4 1;396 A4 4 1;398 F#5 4 1;400 E5 4 1;402 C5 4 1;404 A4 4 1;400 F4 4 1;406 E5 4 1;408 B4 4 1;409 C5 4 1;410 A4 4 1;412 A3 4 1;414 B3 4 1;416 C4 4 1;418 E4 4 1;420 G4 4 1;422 C5 4 1;424 G3 4 1;424 G5 4 1;424 G4 4 1;426 D5 4 1;428 G4 4 1;430 G5 4 1;432 G5 4 1;433 F#5 4 1;432 D4 4 1;448 C4 4 1;448 C5 4 1;450 E4 4 1;452 G4 4 1;454 C5 4 1;456 F#5 4 1;456 D4 4 1;458 D5 4 1;460 A4 4 1;462 F#5 4 1;464 E5 4 1;466 C5 4 1;468 A4 4 1;464 F4 4 1;470 E5 4 1;472 B4 4 1;473 C5 4 1;474 A4 4 1;444 A3 4 1;446 B3 4 1;476 A4 4 1;478 B4 4 1;480 C5 4 1;476 A3 4 1;478 B3 4 1;480 C4 4 1;482 E4 4 1;484 G4 4 1;486 C5 4 1;488 D4 4 1;490 D5 4 1;492 A4 4 1;494 E5 2 1;432 D5 2 1;432 G4 2 1;434 D5 2 1;436 D5 4 1;434 F#5 2 1;436 F#5 4 1;496 E5 2 1;498 E5 2 1;500 E5 2 1;496 C5 2 1;498 C5 2 1;500 C5 2 1;496 A4 2 1;498 A4 2 1;500 A4 2 1;496 F4 2 1;498 F4 2 1;80 C6 4 23;240 D6 2 23;240 G5 2 23;240 B5 2 23;242 A5 6 23;242 C6 6 23;242 E6 6 23;500 F4 2 1;220 C7 4 23;64 A3 8 23;72 G#3 8 23;80 G3 8 23;88 F#3 8 23;96 F3 16 23;128 C3 8 23;136 D3 8 23;144 F3 8 23;152 E3 8 23;160 C3 8 23;168 G3 8 23;176 F#3 8 23;192 C4 8 23;200 D4 8 23;208 F4 8 23;216 E4 8 23;88 C6 4 23;88 A5 4 23;92 C6 4 23;92 A5 4 23;132 E6 4 23;140 F#6 4 23;140 D6 4 23;132 C6 4 23;132 G5 4 23;140 A5 4 23;164 E6 4 23;164 C6 4 23;164 G5 4 23;172 D6 2 23;172 E6 2 23;172 G5 2 23;84 A5 4 23;84 C6 4 23'

song = '3 F#5 1 18;4 F#6 1 18;5 C#6 1 18;6 A5 1 18;7 F#5 1 18;8 F6 1 18;9 C#6 1 18;10 A5 1 18;11 F#5 1 18;12 F#6 1 18;13 C#6 1 18;14 A5 1 18;15 F#5 1 18;16 F#6 1 18;17 B5 1 18;18 G#5 1 18;19 E5 1 18;20 E6 1 18;21 B5 1 18;22 G#5 1 18;23 E5 1 18;24 D#6 1 18;25 B5 1 18;26 G#5 1 18;27 E5 1 18;28 E6 1 18;29 B5 1 18;30 G#5 1 18;31 E5 1 18;32 E6 1 18;33 A5 1 18;34 F#5 1 18;35 D#5 1 18;36 D#6 1 18;37 A5 1 18;38 F#5 1 18;39 D#5 1 18;40 D6 1 18;41 A5 1 18;42 F#5 1 18;43 D#5 1 18;44 D#6 1 18;45 A5 1 18;46 F#5 1 18;47 D#5 1 18;48 D#6 1 18;49 G#5 1 18;50 E5 1 18;51 C#5 1 18;52 C#6 1 18;56 C6 1 18;53 G#5 1 18;54 E5 1 18;55 C#5 1 18;57 G#5 1 18;58 E5 1 18;59 C#5 1 18;60 C#6 1 18;61 G#5 1 18;62 E5 1 18;63 C#5 1 18;64 G#6 1 18;68 F#6 1 18;72 F6 1 18;76 F#6 1 18;80 A6 1 18;84 G#6 1 18;88 G6 1 18;92 G#6 1 18;65 C#6 1 18;66 A5 1 18;67 F#5 1 18;69 C#6 1 18;70 A5 1 18;71 F#5 1 18;73 C#6 1 18;74 A5 1 18;75 F#5 1 18;77 C#6 1 18;78 A5 1 18;79 F#5 1 18;81 D6 1 18;82 B5 1 18;83 F5 1 18;85 D6 1 18;86 B5 1 18;87 F5 1 18;89 D6 1 18;90 B5 1 18;91 F5 1 18;93 D6 1 18;94 B5 1 18;95 F5 1 18;96 B6 1 18;100 A6 1 18;104 G#6 1 18;108 A6 1 18;112 G#6 1 18;116 F#6 1 18;120 E6 1 18;124 D#6 1 18;97 C#6 1 18;98 A5 1 18;99 F#5 1 18;101 C#6 1 18;102 A5 1 18;103 F#5 1 18;105 C#6 1 18;106 A5 1 18;107 F#5 1 18;109 C#6 1 18;110 A5 1 18;111 F#5 1 18;113 A5 1 18;114 F#5 1 18;115 D#5 1 18;117 A5 1 18;118 F#5 1 18;119 D#5 1 18;121 A5 1 18;122 F#5 1 18;123 D#5 1 18;125 A5 1 18;126 F#5 1 18;127 D#5 1 18;1 C#4 1 18;2 F#4 1 18;3 G#4 1 18;9 C#4 1 18;10 G#4 1 18;11 F#4 1 18;12 B4 1 18;13 G#4 1 18;14 F#4 1 18;15 C#4 1 18;17 G#3 1 18;18 B3 1 18;19 F#4 1 18;25 G#3 1 18;26 F#4 1 18;27 E4 1 18;28 B4 1 18;29 F#4 1 18;30 E4 1 18;31 B3 1 18;34 A3 1 18;33 G#3 1 18;32 F#3 1 18;35 E4 1 18;32 G3 8 20;40 G3 8 20;16 A3 8 20;24 A3 8 20;48 F3 8 20;56 F3 8 20;64 A#3 8 20;88 D4 8 20;96 G3 8 20;104 G3 8 20;120 C4 8 20;64 A6 4 11;68 G6 4 11;72 F#6 4 11;76 G6 4 11;80 A#6 4 11;84 A6 4 11;88 G#6 4 11;92 A6 4 11;96 C7 4 11;100 A#6 4 11;104 A6 4 11;108 A#6 4 11;112 A6 4 11;116 G6 4 11;120 F6 4 11;124 E6 4 11;0 G#6 1 18;41 F#3 1 18;42 E4 1 18;43 D#4 1 18;44 F#4 1 18;45 D#4 1 18;46 B3 1 18;47 A3 1 18;49 E3 1 18;50 G#3 1 18;51 D#4 1 18;57 G#3 1 18;58 D#4 1 18;59 C#4 1 18;60 F#4 1 18;61 E4 1 18;62 B4 1 18;63 A4 1 18;0 A3 1 18;64 A3 1 18;65 C#4 1 18;66 F#4 1 18;67 G#4 1 18;73 C#4 1 18;74 G#4 1 18;75 F#4 1 18;76 C#5 1 18;77 G#4 1 18;78 F#4 1 18;79 C#4 1 18;81 G#3 1 18;82 G#4 1 18;83 B4 1 18;89 C#4 1 18;90 B4 1 18;91 G#4 1 18;92 D5 1 18;93 C#5 1 18;94 B4 1 18;95 G#4 1 18;97 F#3 1 18;98 F#4 1 18;99 A4 1 18;105 F#3 1 18;106 A4 1 18;107 G#4 1 18;108 B4 1 18;109 A4 1 18;110 F#4 1 18;111 C#4 1 18;113 B3 1 18;114 F#4 1 18;115 D#5 1 18;121 B3 1 18;122 A4 1 18;123 F#4 1 18;124 D#5 1 18;125 C#5 1 18;2 A5 1 18;1 C#6 1 18;126 F#4 1 18;127 C#4 1 18;72 A#3 8 20;80 A3 8 20;112 C4 8 20;0 A#3 8 20'
#song = '0 A4 1 43;2 A4 1 43;4 C5 1 43;5 A4 1 43;8 A5 1 43;10 A5 1 43;11 G#5 3 43;16 A4 1 43;18 A4 1 43;20 C5 1 43;23 A4 1 43;24 G5 1 43;26 G5 1 43;27 F#5 3 43;32 E5 1 43;34 E5 1 43;36 G5 1 43;37 E5 1 43;42 E6 1 43;43 D#6 3 43;40 E6 1 43;48 E5 1 43;50 E5 1 43;52 G5 1 43;55 E5 1 43;56 D6 1 43;58 D6 1 43;59 C#6 3 43;32 E5 14 41;7 A4 1 43;21 A4 1 43;39 E5 1 43;53 E5 1 43;0 A3 1 41;2 A3 1 41;8 A3 1 41;10 A3 1 41;16 A3 1 41;18 A3 1 41;24 A3 1 41;26 A3 1 41;28 A3 1 41;30 A3 1 41;32 E4 1 41;32 E4 1 41;34 E4 1 41;40 E4 1 41;42 E4 1 41;48 E4 1 41;50 E4 1 41;56 E4 1 41;58 E4 1 41;60 E4 1 41;62 E4 1 41;20 A3 1 41;22 A3 1 41;52 E4 1 41;54 E4 1 41'
#song = '0 G5 1 43;1 G#5 1 43;3 A#5 1 43;4 B5 1 43;6 C#6 1 43;7 D#6 1 43;9 E6 1 43;10 D#6 1 43;13 B5 1 43;19 B5 1 43;16 D#6 1 43;24 D#6 1 43;25 D6 1 43;27 D#6 1 43;28 D6 1 43;30 D#6 1 43;31 D6 1 43;33 D#6 1 43;34 B5 1 43;37 G#5 1 43;48 G5 1 43;49 G#5 1 43;51 A#5 1 43;52 B5 1 43;54 C#6 1 43;55 D#6 1 43;57 E6 1 43;58 D#6 1 43;61 B5 1 43;67 B5 1 43;64 D#6 1 43;72 G#6 1 43;73 F#6 1 43;75 D#6 1 43;76 C#6 1 43;78 F#6 1 43;79 D#6 1 43;81 B5 1 43;82 G#5 1 43;40 B5 1 43;85 G#5 1 43;88 B5 1 43;91 G#5 1 43;96 G5 1 43;97 G#5 1 43;99 A#5 1 43;100 B5 1 43;102 C#6 1 43;103 D#6 1 43;105 E6 1 43;106 D#6 1 43;109 E6 1 43;112 D#6 1 43;114 E6 1 43;117 D#6 1 43;121 C#6 1 43;124 B5 1 43;127 A#5 1 43;133 C#6 1 43;136 D#6 1 43;138 B5 1 43;141 G#5 1 43;130 B5 1 43;147 B5 1 43;150 B5 1 43;153 B5 1 43;156 B5 1 43;159 B5 1 43;162 B5 1 43;165 A#5 1 43;167 B5 1 43;170 A#5 1 43;178 D#6 1 43;181 C#6 1 43;183 D#6 1 43;184 B5 1 43;186 C#6 1 43;187 A#5 1 43;189 B5 1 43;43 G#5 1 43;180 E6 1 43;190 G#5 1 43'
mySong = music(song, pins=[Pin(0)])
names = ["uno","dos","tres"]
#Four buzzers
#mySong = music(song, pins=[Pin(0),Pin(1),Pin(2),Pin(3)])

def play():
    print(mySong.tick())    
    sleep(0.04)



booly = True
while booly:
    play()
 ```
 
 Código para la libreria
 
  ``` Python
  from machine import Pin, PWM
from math import ceil

tones = {
    'C0':16,
    'C#0':17,
    'D0':18,
    'D#0':19,
    'E0':21,
    'F0':22,
    'F#0':23,
    'G0':24,
    'G#0':26,
    'A0':28,
    'A#0':29,
    'B0':31,
    'C1':33,
    'C#1':35,
    'D1':37,
    'D#1':39,
    'E1':41,
    'F1':44,
    'F#1':46,
    'G1':49,
    'G#1':52,
    'A1':55,
    'A#1':58,
    'B1':62,
    'C2':65,
    'C#2':69,
    'D2':73,
    'D#2':78,
    'E2':82,
    'F2':87,
    'F#2':92,
    'G2':98,
    'G#2':104,
    'A2':110,
    'A#2':117,
    'B2':123,
    'C3':131,
    'C#3':139,
    'D3':147,
    'D#3':156,
    'E3':165,
    'F3':175,
    'F#3':185,
    'G3':196,
    'G#3':208,
    'A3':220,
    'A#3':233,
    'B3':247,
    'C4':262,
    'C#4':277,
    'D4':294,
    'D#4':311,
    'E4':330,
    'F4':349,
    'F#4':370,
    'G4':392,
    'G#4':415,
    'A4':440,
    'A#4':466,
    'B4':494,
    'C5':523,
    'C#5':554,
    'D5':587,
    'D#5':622,
    'E5':659,
    'F5':698,
    'F#5':740,
    'G5':784,
    'G#5':831,
    'A5':880,
    'A#5':932,
    'B5':988,
    'C6':1047,
    'C#6':1109,
    'D6':1175,
    'D#6':1245,
    'E6':1319,
    'F6':1397,
    'F#6':1480,
    'G6':1568,
    'G#6':1661,
    'A6':1760,
    'A#6':1865,
    'B6':1976,
    'C7':2093,
    'C#7':2217,
    'D7':2349,
    'D#7':2489,
    'E7':2637,
    'F7':2794,
    'F#7':2960,
    'G7':3136,
    'G#7':3322,
    'A7':3520,
    'A#7':3729,
    'B7':3951,
    'C8':4186,
    'C#8':4435,
    'D8':4699,
    'D#8':4978,
    'E8':5274,
    'F8':5588,
    'F#8':5920,
    'G8':6272,
    'G#8':6645,
    'A8':7040,
    'A#8':7459,
    'B8':7902,
    'C9':8372,
    'C#9':8870,
    'D9':9397,
    'D#9':9956,
    'E9':10548,
    'F9':11175,
    'F#9':11840,
    'G9':12544,
    'G#9':13290,
    'A9':14080,
    'A#9':14917,
    'B9':15804
}

#Time, Note, Duration, Instrument (onlinesequencer.net schematic format)
#0 D4 8 0;0 D5 8 0;0 G4 8 0;8 C5 2 0;10 B4 2 0;12 G4 2 0;14 F4 1 0;15 G4 17 0;16 D4 8 0;24 C4 8 0

class music:
    def __init__(self, songString='0 D4 8 0', looping=True, tempo=3, duty=2512, pin=None, pins=[Pin(0)]):
        self.tempo = tempo
        self.song = songString
        self.looping = looping
        self.duty = duty
        
        self.stopped = False
        
        self.timer = -1
        self.beat = -1
        self.arpnote = 0
        
        self.pwms = []
        
        if (not (pin is None)):
            pins = [pin]
        self.pins = pins
        for pin in pins:
            self.pwms.append(PWM(pin))
        
        self.notes = []

        self.playingNotes = []
        self.playingDurations = []


        #Find the end of the song
        self.end = 0
        splitSong = self.song.split(";")
        for note in splitSong:
            snote = note.split(" ")
            testEnd = round(float(snote[0])) + ceil(float(snote[2]))
            if (testEnd > self.end):
                self.end = testEnd
                
        #Create empty song structure
        while (self.end > len(self.notes)):
            self.notes.append(None)

        #Populate song structure with the notes
        for note in splitSong:
            snote = note.split(" ")
            beat = round(float(snote[0]));
            
            if (self.notes[beat] == None):
                self.notes[beat] = []
            self.notes[beat].append([snote[1],ceil(float(snote[2]))]) #Note, Duration


        #Round up end of song to nearest bar
        self.end = ceil(self.end / 8) * 8
    
    def stop(self):
        for pwm in self.pwms:
            pwm.deinit()
        self.stopped = True

    def restart(self):
        self.beat = -1
        self.timer = 0
        self.stop()
        self.pwms = []
        for pin in self.pins:
            self.pwms.append(PWM(pin))
        self.stopped = False

    def resume(self):
        self.stop()
        self.pwms = []
        for pin in self.pins:
            self.pwms.append(PWM(pin))
        self.stopped = False

    def tick(self):
        if (not self.stopped):
            self.timer = self.timer + 1
            
            #Loop
            if (self.timer % (self.tempo * self.end) == 0 and (not (self.timer == 0))):
                if (not self.looping):
                    self.stop()
                    return False
                self.beat = -1
                self.timer = 0
            
            #On Beat
            if (self.timer % self.tempo == 0):
                self.beat = self.beat + 1

                #Remove expired notes from playing list
                i = 0
                while (i < len(self.playingDurations)):
                    self.playingDurations[i] = self.playingDurations[i] - 1
                    if (self.playingDurations[i] <= 0):
                        self.playingNotes.pop(i)
                        self.playingDurations.pop(i)
                    else:
                        i = i + 1
                        
                #Add new notes and their durations to the playing list
                
                """
                #Old method runs for every note, slow to process on every beat and causes noticeable delay
                ssong = song.split(";")
                for note in ssong:
                    snote = note.split(" ")
                    if int(snote[0]) == beat:
                        playingNotes.append(snote[1])
                        playingDurations.append(int(snote[2]))
                """
                
                if (self.beat < len(self.notes)):
                    if (self.notes[self.beat] != None):
                        for note in self.notes[self.beat]:
                            self.playingNotes.append(note[0])
                            self.playingDurations.append(note[1])
                
                #Only need to run these checks on beats
                i = 0
                for pwm in self.pwms:
                    if (i >= len(self.playingNotes)):
                        pwm.duty_u16(0)
                    else:
                        #Play note
                        pwm.duty_u16(self.duty)
                        pwm.freq(tones[self.playingNotes[i]])
                    i = i + 1
            

            #Play arp of all playing notes
            if (len(self.playingNotes) > len(self.pwms)):
                self.pwms[len(self.pwms)-1].duty_u16(self.duty)
                if (self.arpnote > len(self.playingNotes)-len(self.pwms)):
                    self.arpnote = 0
                self.pwms[len(self.pwms)-1].freq(tones[self.playingNotes[self.arpnote+(len(self.pwms)-1)]])
                self.arpnote = self.arpnote + 1
                
            return True
        else:
            return False
 
 ```
 
 ### 12. KY-015 (TEMP AND HUMIDITY)

Descripción: El módulo DHT11 o KY-015 es un sensor de temperatura y humedad de salida de señal digital, tiene un tamaño ultra compacto, es de bajo consumo de energía y tiene gran utilidad cuando se requiere detectar dos magnitudes al mismo tiempo.



 ``` Python
 from machine import Pin
from time import sleep
import dht
 
sensor = dht.DHT22(Pin(2)) 
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    sleep(2)
 ```
### 13. RGB LED

Descripción: El LED RGB es un tipo especial de diodo LED que se compone por varias matrices LEDs simples como las que se encuentran en otros LEDs monocolor. De esa forma, pueden emitir en estos tres colores primarios, generando así todo tipo de efectos y colores diferentes (incluso el blanco combinando el rojo, verde y azul a la vez) tan solo controlando una de las patillas de estos componentes.



 ``` Python
 from machine import Pin
from time import sleep

btn = Pin(10,Pin.IN,Pin.PULL_UP)

while True:
    if btn.value()== 0:
        print(a)
 ```
 
 ### 14. TILT SWITCH

Descripción: Un Tilt Switch o interruptor basculante es un tipo de interruptor o sensor de inclinación que cambia en un cierto ángulo en comparación con el horizonte (similar al antiguo interruptor de mercurio). Se trata de un inclinómetro con salida de conmutación. Dado que la gravedad sirve como referencia, se consigue la máxima libertad de montaje.



 ``` Python
 from machine import Pin
import time

TiltSensor = Pin(17, Pin.IN)

while True:
    value = TiltSensor.value()
    print(value, end = " ")
    if  value== 0:
        print("The switch is turned on")
    else:
        print("The switch is turned off")
    time.sleep(0.1)
 ```
 
 ### 15. KY-018 (Photoresistor)

Descripción: El módulo de fotorresistencia KY-018 se utiliza para medir la intensidad de la luz. La resistencia disminuirá en presencia de luz y aumentará en ausencia de ella. La salida es analógica y determina la intensidad de la luz.



 ``` Python
 from machine import ADC, Pin
from time import sleep

photoPIN = 26

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    
    light = photoRes.read_u16()
    light = round(light/65535*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) + "%")
    sleep(1)
 ```
 
 ### 16. KY-019 (Relay)

Descripción: El sensor KY-019 (Relay) es un módulo electrónico que incluye un relé electromagnético. Este módulo se utiliza para controlar dispositivos de alto voltaje o corriente utilizando señales de baja potencia provenientes de microcontroladores u otros circuitos electrónicos.



 ``` Python
 from machine import Pin
import utime

relay = Pin(18,Pin.OUT)

while True:
    
    relay.value(1)
    utime.sleep(0.5)
    relay.value(0)
    utime.sleep(0.5)
 ```
 ### 17. BALL SWITCH

Descripción: El "sensor ball switch" es un tipo de interruptor o sensor que se activa mediante el movimiento de una bola metálica en su interior. Este tipo de sensor consiste en una carcasa que contiene una pequeña bola metálica y un interruptor en su base. Cuando la carcasa se inclina o se produce un movimiento suficiente, la bola metálica se mueve y hace contacto con el interruptor, cerrando o abriendo el circuito eléctrico.



 ``` Python
 from machine import Pin
import time

BallSensor = Pin(17, Pin.IN)

while True:
    value = BallSensor.value()
    print(value, end = " ")
    if  value== 0:
        print("The ball is moving...")
    else:
        print("The ball isn't moving...")
    time.sleep(0.1)
 ```
 
 ### 18. MINI SWITCH

Descripción: 
Un "mini switch" se refiere a un interruptor de tamaño pequeño. Un interruptor, en general, es un dispositivo eléctrico que permite abrir o cerrar un circuito para controlar el flujo de corriente eléctrica.



 ``` Python
 from machine import Pin
import utime

pin=16
sensor=Pin(pin, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Switch Apagado")
        utime.sleep(1)    
    else:
        print("Switch Encendido")
        utime.sleep(1)
utime.sleep(1)

 ```
 ### 19. KY-022 (IR RECEIVER)

Descripción: El Sensor Receptor Infrarrojo IR es un módulo KY-022 que esta construido de un receptor IR TL1838, el cual reacciona a la luz infrarroja de 38 KHz y funciona en conjunto con el emisor KY-005.



 ``` Python
 from machine import Pin
import time

pico_led = Pin(25, Pin.OUT)
ir = Pin(15, Pin.OUT)
receiver = Pin(16, Pin.IN)


while True:
    ir.value(1)
    
    #Cuando el sensor recibe un valor se prende el led de la Pico
    if(receiver.value() == 1):
        pico_led.value(1)
    else:
        pico_led.value(0)
        
    time.sleep(1)
 ```
 
 ### 20. JOYSTICK

Descripción: El Módulo KY-023 Sensor JoyStick es un dispositivo electromecánico consta de dos potenciómetros en un ángulo de 90 grados. Este elemento te permite controlar y manejar determinados aparatos electrónicos. Normalmente se utilizan para proyectos robóticos en el cual se necesitan para la movilidad analógica de las articulaciones de un brazo robótico. El Módulo Joystick, es más utilizado para proyectos de robótica y control de dispositivos RF(Radio Frecuencia)NRF24L01.



 ``` Python
 from machine import Pin, ADC
import utime#libs

xAxis = ADC(Pin(27))#pin adc 27 para el ejex del pinout del joystick
yAxis = ADC(Pin(26))#pin adc 26 para el ejey del pinout del joystick
button = Pin(16,Pin.IN, Pin.PULL_UP)#pin 16 para el boton del joystick, syntax de analog input
while True:#loop
    xValue = xAxis.read_u16()#catch x value
    yValue = yAxis.read_u16()#catch y value
    buttonValue = button.value()#catch btn value
    if xValue <= 600:#si el valor es de 600 (llega hasta 65K) o menos, se interpreta como Left
        xStatus = "left"
        print(xStatus)
    elif xValue >= 60000:#al pasar el valor de 60k se interpeta como right
        xStatus = "right"
        print(xStatus)
    if yValue <= 600:#up y down funcionan similar pero con el pin 26
        yStatus = "up"
        print(yStatus)
    elif yValue >= 60000:
        yStatus = "down"
        print(yStatus)
    if buttonValue == 0:#al ser un digital input muy simple, maneja 0 y 1, donde 1 es not pressed, pero no lo escribe porque seria un spam en la terminal
        buttonStatus = "pressed"
        print(buttonStatus)
        #despues de cada detect de cambios, se imprime el valor si se cumple la condicion
    utime.sleep(0.1)#ritmo con el que se busca un cambio en los valores x, y y el btn

 ```
 
### 21. KY-025 (Reed Switch)

Descripción: El sensor KY-025 (Reed Switch) es un módulo electrónico que incorpora un interruptor de lengüeta (reed switch) en su diseño. Este sensor se utiliza para detectar la presencia o ausencia de un campo magnético.



 ``` Python
 from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("A magnetic field")
    else:
        print("There is no magnetic field")
    time.sleep(0.1)
 ``` 
 
 ### 22. KY-026 (FLAME)

Descripción: El sensor KY-026 (FLAME) es un módulo electrónico diseñado para detectar la presencia de fuego o llamas. Este sensor se utiliza para detectar incendios o flamas en aplicaciones de seguridad o control.

El sensor KY-026 utiliza un sensor de llama sensible a la radiación infrarroja emitida por una fuente de fuego. Cuando se detecta la presencia de una flama, el sensor genera una señal de salida que puede ser utilizada para activar una alarma, un sistema de extinción de incendios u otros dispositivos de seguridad.



 ``` Python
 from machine import Pin#pin lib
import time#time lib

flame = Pin(0,Pin.IN)#analog input
    
while True:#loop 
    if flame.value() == 0:#en analog input, el valor default es 1, al detectar fuego se vuelve 0
        print("fuego!")#alerta en terminal
        time.sleep(1)#sleep de 1 segundo para no saturar la terminal
 ```
 
 ### 23. MINI TWO-COLOR


 ``` Python
 from machine import Pin
import time

led_pins = [16,17]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.2
while True:
    for led in leds:
        led.high()
        time.sleep(delay_t)
        led.low()
        time.sleep(delay_t)
 ```
 
 ### 24. TAP MODULE
 


 ``` Python
 import time
from machine import Pin

pico_led = Pin(25, Pin.OUT)
knock = Pin(16, Pin.IN)

while True:
    if(knock.value() == 1):
        pico_led.value(1)
        time.sleep(2)
    else:
        pico_led.value(0)
        time.sleep(2)
 ```
 
 ### 25. AVOIDANCE

Descripción: se refiere a un tipo de sensor utilizado para evitar obstáculos o colisiones en aplicaciones robóticas o de navegación autónoma. Estos sensores están diseñados para detectar la presencia de objetos cercanos y enviar señales de advertencia o control para evitarlos.



 ``` Python
 from machine import Pin
import time

sensor = Pin(16, Pin.IN)
while True:
    if sensor.value() == 0:
        print("There are obstacles")
    else:
        print("All going well")
    time.sleep(0.1)
 ```
 
 ### 26. KY-033 (Tracking)

Descripción: Este es básicamente un módulo de detección de obstáculos que tiene un receptor y transmisor incorporados que detecta la energía IR y busca la energía IR reflejada para detectar el obstáculo frente al módulo sensor. El sensor devuelve el estado de la luz IR reflejada desde la superficie. Así que es un dispositivo bastante simple, tiene un receptor de infrarrojos y un transmisor de infrarrojos. 



 ``` Python
 from machine import Pin
import time

sensor = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if sensor.value() == 0:
        print("0   White")
    else:
        print("1   Black")
    time.sleep(0.1)
 ```
 
 ### 27. 7 COLOR FLASH

Descripción: El "sensor 7 color flash" se refiere a un módulo o dispositivo que combina un sensor de luz con capacidades de destello o cambio de color. Este tipo de sensor está diseñado para detectar la intensidad de la luz en el entorno y emitir destellos o cambios de color en respuesta a las variaciones de luz detectadas.



 ``` Python
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
 ```
 
 ### 28. KY-036 (Touch)

Descripción: El sensor KY-036 (Touch) es un módulo electrónico diseñado para detectar el contacto físico o la presión aplicada por un objeto. Este sensor se utiliza para detectar toques o interacciones táctiles en aplicaciones como pantallas táctiles, paneles de control o interruptores sensibles al tacto.



 ``` Python
 from machine import Pin
import time

button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 1:
        print("You pressed the button!")
    else:
        print("You loosen the button!")
    time.sleep(0.1)
 ```
 
 ### 29. KY-037 (Big Sound)

Descripción: El sensor KY-037 (Big Sound) es un módulo electrónico diseñado para detectar sonidos o ruidos de mayor amplitud o intensidad en el entorno. Este sensor se utiliza para captar y medir sonidos fuertes o sonidos de baja frecuencia.



 ``` Python
 from machine import Pin, ADC
from time import sleep

buzzer = Pin(16, Pin.OUT, value=0)

sensor = ADC(0)

while True:
    value = sensor.read_u16()
    print(value)
    sleep(0.5)
 ```
 
  ### 30. KY-038 (Small Sound)

Descripción: El sensor KY-038 (Small Sound) es un módulo electrónico que se utiliza para detectar y medir sonidos o ruidos pequeños en el entorno. Este sensor es sensible a las vibraciones acústicas y se utiliza en aplicaciones donde se necesita detectar la presencia o intensidad de sonidos.



 ``` Python
 from machine import Pin, ADC
from time import sleep

buzzer = Pin(16, Pin.OUT, value=0)

sensor = ADC(0)

while True:
    value = sensor.read_u16()
    print(value)
    sleep(0.5)
 ```
 
  ### 31. HEARTBEAT

Descripción: El sensor de latidos del corazón, también conocido como sensor de pulso o sensor de frecuencia cardíaca, es un dispositivo que se utiliza para medir y detectar las pulsaciones del corazón de una persona.



 ``` Python
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
 ```
 
  ### 32. ROTARY ENCODER

Descripción: Un "sensor rotary encoder" es un dispositivo electromecánico utilizado para medir la posición y la dirección de rotación de un eje. Consiste en un disco o dial con marcas o ranuras equidistantes en su perímetro y un conjunto de sensores ópticos o magnéticos.



 ``` Python
 from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from picozero import RGBLED
import utime
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import utime

WIDTH  = 128                                         
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
rgb = RGBLED(red=16,green=18,blue=20)
dtpin = Pin(14,Pin.IN,Pin.PULL_UP)
clpin = Pin(15,Pin.IN,Pin.PULL_UP)
rbtn = Pin(13,Pin.IN,Pin.PULL_UP)

value = True
pvalue = False
rvalue = 0
gvalue = 0
bvalue = 0
cycle = "r"
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
writeuwu = Write(oled, ubuntu_mono_20)
def rotary_changed():
    oled.fill(0)
    global pvalue
    global value
    global rvalue,gvalue,bvalue
    global cycle
    if rvalue < 0:
        rvalue = 0
    elif rvalue > 255:
        rvalue == 255
    if gvalue < 0:
        gvalue = 0
    elif gvalue > 255:
        gvalue == 255
    if bvalue < 0:
        bvalue = 0
    elif bvalue > 255:
        bvalue == 255
    if pvalue != clpin.value():
        if clpin.value() == False:
            if dtpin.value() == False:
                if cycle == "r":
                    if rvalue < 255:
                       rvalue = rvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "g":
                    if gvalue < 255:
                       gvalue = gvalue + 5
                    else:
                        print("already 255!")
                        
                elif cycle == "b":
                    if bvalue < 255:
                       bvalue = bvalue + 5
                    else:
                        print("already 255!")
                        
                rgb.color = (rvalue,gvalue,bvalue)
            else:
                if cycle == "r":
                    if rvalue > 0:
                       rvalue = rvalue - 5
                    else:
                        print("already 0!")
                        
                elif cycle == "g":
                    if gvalue > 0:
                       gvalue = gvalue - 5
                    else:
                        print("already 0!")
                elif cycle == "b":
                    if bvalue > 0:
                       bvalue = bvalue - 5
                    else:
                        print("already 0!")
                rgb.color = (rvalue,gvalue,bvalue)
        pvalue = clpin.value()
        writeuwu.text("Red: ", 20, 0)
        writeuwu.text("Green: ", 0, 20)
        writeuwu.text("Blue: ", 10, 40)
        
        writeuwu.text(str(rvalue),60,0)
        writeuwu.text(str(gvalue),60,20)
        writeuwu.text(str(bvalue),60,40)
        oled.show()
    if rbtn.value() == 0:       
        if cycle == "r":
            cycle = "g"
        elif cycle == "g":
            cycle = "b"
        elif cycle == "b":
            cycle = "r"
        utime.sleep(1)
        

while True:
   rotary_changed()
 ```

### 33. KY-035 (ANALOG HALL)

Descripción: El sensor de efecto Hall Analog 49E puede detectar el polo magnético y la fuerza relativa de un campo magnético. En el caso de nuestro módulo, envía una señal analógica cada vez que detecta un campo magnético cercano. Si no hay campo magnético, la señal analógica es la mitad del Vcc.



 ``` Python
import RPi.GPIO as GPIO
import time
sensor_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

while True:
    value = GPIO.input(sensor_pin)
    print(value)
    time.sleep(0.1)

   ```
