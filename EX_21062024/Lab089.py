#Unpacking of tuple

a, b ,c = (12, 34, 56)


t = (12, 34, 56)
# t.append() #tuple are immutable in nature so this append is not possible
new_t = t + (5,)
print(new_t) # this will add item but it will create new tuple

my_list = list(t)
print(my_list)
my_list.append(5)
new_t2 = tuple(my_list)
print(new_t2)

#in above code we have converted tuple to list then appended list and then again converted back to tuple