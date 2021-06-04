from math import factorial
from itertools import count
def fact():
    for x in count(1):
        yield factorial(x)

for pos, i in enumerate(fact(), start=1):
    print('{} - {}'.format(pos, i))
    if pos == 10:
        break