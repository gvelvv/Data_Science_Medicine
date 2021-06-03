int_dict = {}
r_dict = {}
with open('hw5_q6.txt') as school:
    for items in school:
        items = items.split(':')
        key_dict = items.pop(0)
        # print(key_dict)
        total = 0
        for sub_items in items:
            sub_items = sub_items.split('(')
            sub_items.pop()
            for ss_items in sub_items:
                ss_items = ss_items.split()
                ss_items.reverse()
                ss_items = ss_items[0]
                total += int(ss_items)
            int_dict = {key_dict: total}
        r_dict.update(int_dict)
    print(r_dict)