"""
Author: João Paulo Andrade
Email: joaopauloap@gmail.com
Script for get range allocated ipv4/ipv6 from lacnic
"""

from ftplib import FTP


class GetTarget:
    # Download of data
    def __init__(self):
        self._ftp = FTP('ftp.lacnic.net')
        self._ftp.login()
        self._ftp.cwd('/pub/stats/lacnic/')
        self._ftp.retrbinary('RETR delegated-lacnic-latest', open('lacnic-latest', 'wb').write)

    @staticmethod
    def gen_target(file):
        # Tranform amount ips in mask CIDR
        def get_mask(amount):
            mask = 0
            while amount != 1:
                amount = amount / 2
                mask += 1
            return 32 - mask

        f = open(file, 'r')
        l_raw = f.readlines()
        l_format = [x.strip().split('|') for x in l_raw]
        for x in l_format:
            if x.__len__() == 7:
                if (x[2] == 'ipv4') and (x[6] == 'allocated'):
                    z = open('ipv4_lacnic', 'a+')
                    z.writelines('{}/{}\n'.format(x[3], get_mask(int(x[4]))))
                    z.close()
        f.close()
