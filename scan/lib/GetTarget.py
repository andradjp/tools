"""
Author: João Paulo Andrade
Email: joaopauloap@gmail.com
Script for get range allocated ipv4/ipv6
****************************************
afrinic - Africa
apnic - Asia
arin - America do Norte
lacnic - America do Sul
ripenic - Europa
*****************************************
"""
from ftplib import FTP

target = 'ripencc'

class GetTarget(object):
    # Download of data
    def __init__(self):
        self._ftp = FTP('ftp.lacnic.net')
        self._ftp.login()
        self._ftp.cwd('/pub/stats/{}/'.format(target))
        self._ftp.retrbinary('RETR delegated-{}-latest'.format(target), open('{}-latest'.format(target), 'wb').write)
        self._file = '{}-latest'.format(target)

    def gen_target(self):
        # Transform amount ips in mask CIDR
        def get_mask(amount):
            mask = 0
            while amount != 1:
                amount = amount / 2
                mask += 1
            return 32 - mask

        f = open(self._file, 'r')
        l_raw = f.readlines()
        l_format = [x.strip().split('|') for x in l_raw]
        for x in l_format:
            if x.__len__() == 7:
                if (x[2] == 'ipv4') and (x[6] == 'allocated'):
                    z = open('ipv4_{}'.format(target), 'a+')
                    z.writelines('{}/{}\n'.format(x[3], get_mask(int(x[4]))))
                    z.close()
        f.close()
