from machine import Pin
import sys

button1 = Pin(9, Pin.IN, Pin.PULL_UP) # built-in button
button2 = Pin(3, Pin.IN, Pin.PULL_UP)  # D1
b1Value = True
b2Value = True

while True:
    if button1.value() != b1Value:
        sys.stdout.write("-1\n" if button1.value() else "+1\n")
        b1Value = button1.value()
    if button2.value() != b2Value:
        sys.stdout.write("-2\n" if button2.value() else "+2\n")
        b2Value = button2.value()