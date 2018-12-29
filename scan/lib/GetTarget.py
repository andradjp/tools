"""
Author: João Paulo Andrade
Email: joaopauloap@gmail.com
Script for get range allocated ipv4/ipv6
****************************************
afrinic - Africa
apnic - Asia
arin - America do Norte
lacnic - America do Sul
ripencc - Europa
*****************************************
"""
from ftplib import FTP
from scan.lib import database

target = 'arin'

class GetTarget(object):
    # Download of data
    def __init__(self):
        self._ftp = FTP('ftp.lacnic.net')
        self._ftp.login()
        self._ftp.cwd('/pub/stats/{}/'.format(target))
        self._ftp.retrbinary('RETR delegated-{}-latest'.format(target), open('{}-latest'.format(target), 'wb').write)
        self._file = '{}-latest'.format(target)
        self.target = target
        self.database = database.DataBase(target+'.db')
        self.database.create_database()

    def gen_target(self):
        # Transform amount ips in mask CIDR
        def get_mask(amount):
            mask = 0
            while amount != 1:
                amount = amount / 2
                mask += 1
            return 32 - mask
        print(self._file)
        f = open(self._file, 'r')
        l_raw = f.readlines()
        l_format = [x.strip().split('|') for x in l_raw]
        for x in l_format:
            if x.__len__() == 7:
                if (x[2] == 'ipv4') and (x[6] == 'allocated'):
                    self.database.insert_data('{}/{}'.format(x[3], get_mask(int(x[4]))))
        self.database.__delete__(self.database)
        f.close()
