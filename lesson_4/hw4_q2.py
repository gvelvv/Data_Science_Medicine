orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
r_list = [j for i, j in enumerate(orig_list) if j > orig_list[i - 1] and i != 0]
print(r_list)