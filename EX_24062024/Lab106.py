#map - it returns normal nos
#pick one item and applly the function
#it will give same no of elements

numbers = [1,2,3,4,5,6,7,8,9,10]

def double_me(num):
    return num*2

new_list_double = map(double_me, numbers)
print(list(new_list_double))

#Filter - only work when with functions which gives true or false
#pick item m if true keep it, and remove it if its false
#it can give less number of items as compared to list

def even_giver(n):
    return n%2 == 0

new_filtered_list = list(filter(even_giver, numbers))
print(new_filtered_list)