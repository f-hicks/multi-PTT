# Multi-PTT firmware

The firmware that runs on microcontrollers connected to physical buttons.

## Prerequisites

- esptool installed
- mpremote installed

## Setup

1. Erase the flash on the microcontroller
```bash
esptool -p COM<x> erase_flash
```
2. Download micropython for your microcontroller.
Find the binary for your microcontroller [here](https://micropython.org/download/). <br>
I am using an ESP32-C3 SuperMini, so i downloaded the latest release (v1.16.1 at time of writing) from [here](https://micropython.org/download/ESP32_GENERIC_C3/).

3. Flash the micropython binary to your microcontroller
```bash
esptool --baud 460800 -p COM<x> write_flash 0 <filename.bin>
```

4. Upload the python files to the microcontroller.
```bash
cd firmware
mpremote connect COM<x> + cp -r . :/
```

5. Reset the microcontroller to start the program.