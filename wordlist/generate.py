from itertools import product
from string import ascii_lowercase, digits, ascii_uppercase



def generate_list(words, keys):
    for x in product(words, repeat=keys):
        print(''.join(x))

def concatenado():
    s = 'test'
    for x in range(1000):
        print(s+str(x))


def default_string(keys):
    for x in range(10**keys):
        print(format(x, '0{}'.format(keys)))

words = digits + ascii_lowercase + ascii_uppercase
generate_list(words, 3)