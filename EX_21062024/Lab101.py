shraddha_details = \
    {"name":"shraddha",
     "90":34.34,
     "isMale":True,
     "address":"KA"
     }

print(shraddha_details.get("address"))
print(shraddha_details["address"])
print(shraddha_details.values())
print(shraddha_details.keys())

my_dict = {'a':1, 'b':2, 'c':3, 'a':95} #keys should be unique , values can be duplicate
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
for i in list(my_dict.values()):
    print(i)

for k,v in my_dict.items():
    print(k,v)