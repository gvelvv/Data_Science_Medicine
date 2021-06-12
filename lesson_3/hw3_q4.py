def my_func (x, y):
    x = x ** y
    print(x)
    return
def my_func_2 (x, y):
    y = abs(y)
    z = 1
    for i in range(1, y+1):
        i += 1
        z = (z * x)
    y = 1 / z
    print(y)
my_func(7, -4)
my_func_2(7, -4)