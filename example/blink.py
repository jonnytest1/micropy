from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)
pin2 = Pin(11, Pin.OUT)
pin2.value(1)
pin.value(0)

while True:
    pin.toggle()
    pin2.toggle()
    sleep(1)
