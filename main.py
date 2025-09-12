import pyautogui
import serial
import voicemeeter
import time

###########################################
#                  Config                 #
###########################################

# The number of hardware buttons you have. Should be between 1 and 5 
# depending on which voicemeeter version is installed.
# voicemeeter basic supports 2 inputs, voicemeeter banana supports 3 inputs, 
# and voicemeeter potato supports 5 inputs.
NUM_BUTTONS: int = 2 

# The serial port the control panel is located on.
SERIAL_PORT: str = "COM12"

# The type of voicemeeter in use. Either "basic", "banana", or "potato"
VOICEMEETER_KIND = "banana"

###########################################

class multiPTT:
    def __init__(self, vmr, numButtons:int = 2):
        if numButtons < 1 or numButtons > 5:
            raise
        else:
            self.outputs = [0]*numButtons
            self.vmr = vmr

    def turnOnMic(self, id: int) -> bool:
        try:
            if not self.outputs[id]:
                self.outputs[id] = True
                pyautogui.keyDown("F13")
                self.vmr.inputs[id].mute = False
            
        except IndexError:
            return False
        else:
            return True
        
    def turnOffMic(self, id: int) -> bool: 
        try: 
            if self.outputs[id]:
                self.outputs[id] = False
                if not any(self.outputs):
                    pyautogui.keyUp("F13")
                    
                self.vmr.inputs[id].mute = True
        
        except IndexError:
            return False
        except Exception:
            return False
        else:
            return True
        

def setup_voicemeeter() -> voicemeeter.remote:
    voicemeeter.launch(VOICEMEETER_KIND, 1)
    vmr = voicemeeter.remote(VOICEMEETER_KIND)
    vmr.login()
    return vmr

def setup_serial() -> serial.Serial:
    return serial.Serial(SERIAL_PORT, 9600)


def main(ptt: multiPTT, ser: serial.Serial) -> None:
    while True:
        try:
            data = str(ser.readline()).replace("b","").replace("'","").replace(r"\r\n","")
            print(data)
            if len(data) >= NUM_BUTTONS:
                for i in range(NUM_BUTTONS):
                    if data[i] == "+":
                        ptt.turnOnMic(i)
                    elif data[i] == "-":
                        ptt.turnOffMic(i)
        except serial.SerialException as e:
            print(e,"\nresetting serial interface\n")
            ser.close()
            time.sleep(1) 
            try:
                ser = setup_serial()
            except Exception as e:
                print(e)
                time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    vmr = setup_voicemeeter()
    ptt = multiPTT(vmr, NUM_BUTTONS)
    ser = setup_serial()
    
    main(ptt, ser)
    