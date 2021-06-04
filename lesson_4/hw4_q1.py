import sys
output_in_hours, rate_per_hour, bonus = sys.argv[1:]
output_in_hours = int(output_in_hours)
rate_per_hour = int(rate_per_hour)
bonus = int(bonus)
salary = output_in_hours * rate_per_hour + bonus
# print(f'salary = {salary}')
print(salary)