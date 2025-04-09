from machine import Pin
import time

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)  # Agrega esta línea

while True:
    led1.on()
    led2.off()  # Agrega esta línea
    time.sleep(1)
    led1.off()
    led2.on()  # Agrega esta línea
    time.sleep(1)
