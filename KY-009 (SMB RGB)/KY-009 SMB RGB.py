from machine import Pin, PWM

red_pin = Pin(15)
green_pin = Pin(14)
blue_pin = Pin(13)

red_pwm = PWM(red_pin)
green_pwm = PWM(green_pin)
blue_pwm = PWM(blue_pin)

red_pwm.duty_ns(0)
green_pwm.duty_ns(0)
blue_pwm.duty_ns(0)