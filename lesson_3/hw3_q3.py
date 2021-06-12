def my_func(*args):
    list_1 = list(args)
    list_1.remove(min(list_1))
    res_1 = list_1[0] * list_1[1]
    print(res_1)
    return
my_func(2, 5, 7)