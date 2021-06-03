import json
with open('hw5_q7.txt') as data_base:
    tot_incom = 0
    profit_firm = 0
    tot_dict = {}
    for data_str in data_base:
        data_str = data_str.split()
        data_str.pop(1)
        comp_name = data_str[0]
        income = int(data_str[1]) - int(data_str[2].rstrip('.'))
        print(f"Corp {comp_name} has income {income}")
        if income > 0:
            tot_incom += income
            profit_firm += 1
            av_income = tot_incom / profit_firm
        com_dict = {comp_name: income}
        tot_dict.update(com_dict)
        av_inc_dict = {'average_profit': av_income}
        r_list = [tot_dict, av_inc_dict]
    print(f"Average incom = {av_income}")
    print(r_list)
    with open('stat_hw5_q7.json', 'w') as r_json:
        json.dump(r_list, r_json)
