from functools import reduce
def mult(*args):
    x = 1
    for i in args:
        x = x * i
    return x
n_list = [i for i in range (100, 1001) if i % 2 == 0]
print(reduce(mult, n_list))
