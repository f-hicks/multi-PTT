from machine import Pin, Signal
from config import PINS
import sys
import time

buttons = []
led = Signal(Pin(8, Pin.OUT, value=1), invert=True)

for pin in PINS:
    buttons.append([Signal(Pin(pin, Pin.IN, Pin.PULL_UP), invert=True), False])

while True:
    string = ""
    for i, button in enumerate(buttons):
        value = button[0].value()
        string = string + str("+" if value else "-")
        button[1] = value
    string = string + "\n"
    sys.stdout.write(string)
    led.value(any([button[1] for button in buttons]))    
    time.sleep(0.001)
