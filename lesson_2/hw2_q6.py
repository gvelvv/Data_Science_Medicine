product_list = []
product = []
analytics = {}
dict_prod_list = []
temp_prod_list = []
analytics_dict = {}
set_value = set()
key_list = input('enter product characteristics separated by a space: ')
key_list = key_list.split()
temp_set = set()
temp_dict = {}
for a in range(1, 10000000):
    product_list = []
    for b in key_list:
        print('enter', b, end='')
        value = input(': ')
        temp_list = [b, value]
        temp_prod_list.append(temp_list)
        dict_prod_list = dict(temp_prod_list)
        temp_list = []
        set_value.add(value)
        analytics_dict.setdefault(b, []).append(value)
        analytics.update({b: list(set(analytics_dict.get(b)))})
    product_list.insert(0, a)
    product_list.insert(1, dict_prod_list)
    tup_1 = tuple(product_list)
    product.append(tup_1)
    for i in product:
        print(i)
    print(analytics)