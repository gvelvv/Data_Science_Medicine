total = 0
with open('hw5_q5.txt', 'w+') as content:
    num = input('enter numbers through a space: ')
    content.write(num)
    content.seek(0)
    nums = content.read().split()
    for i in nums:
        i = int(str(i))
        total += i
    print(total)
