#! micropython
from secrets import WIFI_SSID, WIFI_PASSWORD
import os

def do_connect():
    import network
    
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))
    
do_connect()
os.dupterm(None, 1)