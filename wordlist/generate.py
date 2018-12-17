from itertools import permutations

def permutation():

    s = 'DIGOS0123456789'
    data = ''
    result = permutations(s, 8)
    for x in result:
        print(data.join(x))

def default_string():
    for x in range(10000000000):
        print(format('{:2}', x))
default_string()