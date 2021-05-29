def sum_f(*args):
    for i in temp_list:
        try:
            i = int(i)
        except ValueError:
            global z
            z = False
            return res_num
        res_list.append(i)
        res_num = sum(res_list)
    return res_num
z = True
res_list = []
while z == True:
    temp_str = input("enter numbers separated by a space: ")
    temp_list = temp_str.split()
    print(sum_f(temp_list))


