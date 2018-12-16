from itertools import permutations

s = 'DIGOS0123456789'
data = ''
result = permutations(s, 8)
for x in result:
    print(data.join(x))
