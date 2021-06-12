res_div = 0
res = 0
def division():
    try:
        res = num_1 / num_2
    except ZeroDivisionError:
        return
    return res
num_1 = float(input('input first digit: '))
num_2 = float(input('input second digit: '))
if num_2 == 0:
    print('annigilation')
res_div = division()
print(res_div)