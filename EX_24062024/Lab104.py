#Filters in Python : Filter always works with function
#The filter() function in Python takes in a function and a list as arguments.
# The function is called for each element in the list.
# If the function returns True, the element is added to the result list.
# If the function returns False, the element is discarded.

#Here's a simple example of how the filter() function works:
# def is_even(x):
#     return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Filter on the above -> even ->
# new_list_Even = [2,4,6,8,10]

def is_even(num):
    return num % 2 == 0

def is_greater_than_5(num):
    return num > 5

new_nos_even = filter(is_even, numbers)
new_nos_greater_than_5 = filter(is_greater_than_5, numbers)
print(list(new_nos_even))
print(list(new_nos_greater_than_5))