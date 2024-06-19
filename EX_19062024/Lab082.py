# list=[1,2,3,4,5]
# print(list*2)

my_list = [1,2,3,4,5]
# temp_list = []
# for i in list:
#     temp = i*2
#     temp_list.append(temp)
# print(temp_list)

#here new list is defined cz its advisible to do so and if we try to change in same list then it will go into infinite loop

def double_the_item(num):
    return num*2

double_the_item = lambda num:num*2

#map() : its a func which takes each item of lits , execute func on it and return the same list

double_list = list(map(double_the_item,my_list))
print(double_list)

double_list = list(map(lambda num: num**2,my_list))
print(double_list)