from itertools import permutations, combinations_with_replacement
from string import ascii_lowercase, digits

def permutation():
    s = ascii_lowercase+digits
    data = ''
    # result = permutations(s, 8) #Nao repete os caracteres
    result = combinations_with_replacement(s, 8)
    for x in result:
        print(data.join(x))

def default_string():
    for x in range(10**8):
        print(format(x, '08'))


# default_string()
permutation()
