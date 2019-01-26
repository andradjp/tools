from itertools import permutations

def permutation():

    s = '0123'
    data = ''
    result = permutations(s, 4)
    for x in result:
        print(data.join(x))

def default_string():
    for x in range(1000000000):
        print(format(x, '08'))

# default_string()
permutation()