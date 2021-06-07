# import
# from less_module import my_funk, pow
import math
import sys
import time

import less_module as lib
# lib.pow(2, 4)
# import time
# # print(time.localtime())
# a = time.time()
# for i in range(10000000):
#     pass
# b = time.time()
# print(b - a)
# print('start')
# time.sleep(2)
# print('go')
# import math
# print(math.floor(2.8))
# print(math.ceil(2.5))
# print(math.pi)
# import sys
# print(sys.path)
# sys.path.insert(0, "path1")
# print('qwe')
# print(sys.argv)
# folder_from, folder_to = sys.argv[1:]
# print(f'Копирую {folder_from} в {folder_to}')
# time.sleep(2)
# print('Done')
# import os
# print(os.getcwd())
# # os.mkdir()
# for i in os.listdir():
#     print(i, os.path.isdir(i))
# old_list = [10, 20, 30]
# # # new_list = [x ** 2 for x in old_list if x % 2 == 0]
# # # print(new_list)
# # new_dict = {x: x ** 2 for x in old_list}
# # print(new_dict)
# new_tuple = (x ** 2 for x in old_list if x % 2 == 0)
# print(new_tuple)
# def generator(i):
#     while True:
#         i += 1
#         yield i
#
# g_obj = generator(1)
# print(g_obj)
# for i in g_obj:
#     print(i)
#     if i > 50:
#         break
# print('cont')
# for i in g_obj:
#     print(i)
#     if i > 60:
#         break
# import random
# random.seed(7)
# # print(random.random())
# # print(random.randint(1, 3))
# print(random.randrange(0, 10, 3))
from functools import reduce, partial
# print(reduce(lambda x, y:x + y + 1, [10, 20, 30]))
# def my_f(p1, p2):
#     return p1 * p2
#
# new_f = partial(my_f, 2)
# print(new_f(3))
from itertools import count, cycle
# for i in count(7):
#     print(i)
#     if i > 15:
#         break
my_list = ['red', 'yellow', 'green', 'yellow']
for i in cycle(my_list):
    print(i)

