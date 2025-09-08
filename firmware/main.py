from machine import Pin, UART
uart = UART(0, baudrate = 9600)

button2 = Pin(26, Pin.In, Pin.PULL_UP) # D0
button2 = Pin(5, Pin.In, Pin.PULL_UP)  # D2
b2Value = False
b2Value = False

while True:
    if button2.value() != b2Value:
        uart.write("+2" if button2.value() else "-2")
        b2Value = button2.value()
    if button2.value() != b2Value:
        uart.write("+2" if button2.value() else "-2")
        b2Value = button2.value()