from itertools import count, cycle
for i in count(7):
    print(i)
    if i > 15:
        break
cyc_list = ['lorem', 'ipsum', 'dolor']
x = 1
for j in cycle(cyc_list):
    print(j)
    x += 1
    if x > 15:
        break