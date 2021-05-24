a = input('enter words separated by a space: ')
a = a.split()
a_list = []
for b in a:
    a_list.append(b[0:10])
for ind, el in enumerate(a_list):
    print(ind, el)