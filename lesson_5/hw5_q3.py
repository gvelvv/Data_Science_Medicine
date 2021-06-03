quant_units = 0
total_dict = {}
with open('hw5_q3.txt') as salary:
    for units in salary:
        money = units.split()
        unit_salary = int(money[1])
        quant_units += 1
        if unit_salary < 20000:
            print(money[0])
        money_dict = {money[0]:int(money[1])}
        total_dict.update(money_dict)
average_salary = sum(total_dict.values()) / quant_units
print(f"average salary: {average_salary}")