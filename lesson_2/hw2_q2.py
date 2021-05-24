#v1
'''a = input('enter a list separated by a space: ')
a = a.split()
r_list = []
n_list = [a[i:i + 2] for i in range(0, len(a), 2)]
for s_list in n_list:
    s_list.reverse()
    r_list.extend(s_list)
print(r_list)'''
#v2
a = input('enter a list separated by a space: ')
a = a.split()
r_list = []
n_list = [a[i:i + 2] for i in range(0, len(a), 2)]
for s_list in n_list:
    r_list.extend(s_list[::-1])
print(r_list)
