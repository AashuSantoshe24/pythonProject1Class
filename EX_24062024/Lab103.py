my_dict = {'a': 2, 'b': 1, 'c': 3}


#To find a key
for k,v in my_dict.items():
    if k == 'b' :
        print("key with name b is found")

#Below is another method to find value of key 'b'

op = 'b' in my_dict
print(op)