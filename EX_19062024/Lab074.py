numbers = [1,2,3] #list , its a collection of item

# def do_something(numbers):
#     numbers.append(4)
#     numbers[0] = 100
#     return  numbers

def do_something(shraddha_list):
    shraddha_list.append(4)
    shraddha_list[0] = 100
    return  shraddha_list

numbers.append(10) #after line no 1 execution will come to this line first and then line no 14 where we are calling the function
l = do_something(numbers)
print(l)


