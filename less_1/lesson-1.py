#q1
num_1 = 23
num_2 = 345
print(num_1, num_2)
print(num_1 + num_2)
num_3 = int(input('Введите певое число: '))
num_4 = int(input('Введите второе число: '))
str_1 = input('напишите что нибудь: ')
str_2 = input('а теперь что нибудь на латыни: ')
print(num_3, num_4, str_1, str_2)
#q2
time_1 = int(input('введите время в секундах: '))
hours_1 = time_1 // 3600
minutes_1 = (time_1 - hours_1*3600) // 60
sec_1 = time_1 - (hours_1 * 3600) - (minutes_1 * 60)
print(f'{hours_1}:{minutes_1}:{sec_1}')
#q3
num_n = int(input('input any number: '))
num_r = num_n * 3 + num_n * 20 + num_n * 100
print(num_r)
#q4
num_q4 = int(input('please enter positive integer: '))
ans_q4 = num_q4 % 10
while num_q4 > 0:
    num_q4 = num_q4 // 10
    int_q4 = num_q4 % 10
    if int_q4 > ans_q4:
        ans_q4 = int_q4
    else: continue
print(ans_q4)
# q5
income = float(input('please enter annual income: '))
expense = float(input('please enter annual expense: '))
if income > expense:
    print('you work with profit')
elif income == expense:
    print('you work to zero')
else:
    print('you are working at a loss')
if income > expense:
    print('profit margin =', (income - expense))
    staff = int(input('enter the number of employees: '))
    print('profit per employee:',((income - expense) / staff))
# q6
a = float(input('enter a: '))
b = float(input('enter b: '))
result = 1
if a > b:
    print('b should be greater than a')
else:
    while b > a:
        a = a * 1.1
        if b >= a:
            result = result + 1
        else:
            continue
print('the athlete will run', (b), 'kilometers', (result + 1), 'days')
