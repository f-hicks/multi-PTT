# multi-PTT

A tool enabling multiple people to talk in online calls using multiple headsets on a single PC.

Uses hardware buttons to trigger push-to-talk for each mic individually using Voicemeeter.

Currently tested with discord as the voice call platform but should work with any platform that allows rebinding the push to talk button.

## Prerequisites

- Voicemeeter installed
- Python 3 installed

## Setup

1. Install the voicemeeter python package
```bash
git clone https://github.com/Freemanium/voicemeeter-remote-python
cd voicemeeter-remote-python
pip install .
```

2. Install the rest of the requirements
```bash
pip install -r requirements.txt
```

3. Set the number of buttons in the config.
This is done by editing the top section of `main.py` and changing the `NUM_BUTTONS` line to the number of buttons on your control panel

4. Set the serial port in the config.
This is done by editing the top section of `main.py` and changing the `SERIAL_PORT` line to the serial port of your control panel. This is usually found in device manager. Make sure the control panel is plugged in with USB first.

5. Set the voicemeeter type in use.
This is done by editing the top section of `main.py` and changing the `VOICEMEETER_KIND` line version of voicemeeter in use. This must be either "basic", "banana", or "potato".

