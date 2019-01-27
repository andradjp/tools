from itertools import permutations, combinations_with_replacement, accumulate
from string import ascii_lowercase, digits

keys = 9

def permutation():
    s = digits
    data = ''
    result = permutations(s, keys) #Nao repete os caracteres
    # result = combinations_with_replacement(s, 4)
    for x in result:
        print(data.join(x))

def default_string():
    for x in range(10**keys):
        print(format(x, '0{}'.format(keys)))


default_string()
# permutation()
