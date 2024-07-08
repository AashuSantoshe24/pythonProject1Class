my_dict = {'b':2, 'w':1, 'c':45, 'a':34}
print(my_dict)

for k, v in my_dict.items():
    print(k,v)



from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od['b'] = 1
od['c'] = 2
od['d'] = 34
print(od)