list_1 = [7, 5, 3, 3, 2]
print(list_1)
while 1 == 1:
    list_1_rev = list_1[::-1]
    a = int(input('enter the number of the rating: '))
    b = a in list_1_rev
    n = 0
    f = len(list_1_rev)
    if b == False:
        if a > list_1[0]:
            n = f
        else:
            for d in list_1_rev:
                if a > d:
                    n += 1
                else:
                    break
        list_1_rev.insert(n, a)
    else:
        c = list_1_rev.index(a)
        list_1_rev.insert(c, a)
    list_1 = list_1_rev[::-1]
    print(list_1)

