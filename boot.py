##################################
### DO NOT EDIT THIS FILE      ###
###                            ###
### MHM4 boot.py V0.2          ###
### Last Updated               ###
### Manjunath.R                ###
### 25 July 2017               ###
###                            ###
### Copyright Minnovation 2017 ###
##################################

import ubinascii, machine
i=0
def mac():
    mac=ubinascii.hexlify(machine.unique_id(),':').decode()
    mac=mac.replace(":","")
    return mac

ap_ssid = "MHM4-"+mac()
print(ap_ssid)

############ ENTER BOOTLOAD MODE ############
############ USER: micro PASSWD: python #####

from network import WLAN

wlan = WLAN()
wlan.init(mode=WLAN.AP, ssid=ap_ssid, auth=(WLAN.WPA2,'AlphaXI0T'), channel=7, antenna=WLAN.INT_ANT)
from machine import Timer

chrono = Timer.Chrono()

chrono.start()

print('PRESS CTL-C TO ENTER REPL')
while chrono.read() < 10:
    i=i+1
    if i > 100000:
        print('PRESS CTL-C TO ENTER REPL',(30-chrono.read()))
        i=0

wlan.deinit()

################# SIGFOX ###################
#from network import Sigfox
#sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)
#ss = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
#ss.setblocking(True)

################# LORA #####################
#from network import LoRa
#lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915)
#sl = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#sl.setblocking(False)
