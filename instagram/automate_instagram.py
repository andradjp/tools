from random import choice
from string import digits

location = []
for y in range(40):
    s = ''
    for x in range(9):
        s += choice(digits)
    location.append(s)
print(location)
