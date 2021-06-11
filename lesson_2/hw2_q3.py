#ver_1
a = int(input('enter the month number: '))
if a == 0 or a > 12:
    print('we have only 12 months')
else:
    year = [12]
    for m in range(1, 12):
        year.append(m)
    n = year.index(a)
if n < 2:
    print('winter')
elif n > 3 and n < 5:
    print('spring')
elif n > 6 and n < 7:
    print('summer')
else:
    print('autumn')
#ver_2
dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn', 5: 'winter'}
a = int(input('enter the month number: '))
c = 0
w = 0
if a == 0 or a > 12:
    print('we have only 12 months')
else:
    season = [0, 1, 2]
    while c < 1:
        c = season.count(a)
        w += 1
        season = [b + 3 for b in season]
print(dict.get(w))





