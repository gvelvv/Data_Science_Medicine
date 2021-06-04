orig_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
r_list = [i for i in orig_list if orig_list.count(i) == 1]
print(r_list)

