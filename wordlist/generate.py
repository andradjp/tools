from itertools import permutations, combinations_with_replacement, starmap, combinations
from string import ascii_lowercase, digits

keys = 8

def permutation():
    x = 'abcdef' + digits
    for x1 in x:
        for x2 in x:
            for x3 in x:
                for x4 in x:
                    for x5 in x:
                        for x6 in x:
                            for x7 in x:
                                for x8 in x:
                                    print('{}{}{}{}{}{}{}{}'.format(x1,x2,x3,x4,x5,x6,x7,x8))


def concatenado():
    s = 'Geovana'
    for x in range(1000):
        print(s+str(x))


def default_string():
    for x in range(10**keys):
        print(format(x, '0{}'.format(keys)))

# default_string()
permutation()
# concatenado()