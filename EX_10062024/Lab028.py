#operators

#assignment operator
# = - assign the value from right to left

name = "Pramod"

# == -> compare operator (bool)
v1 = (1==True)
v2 = (0==False)
print(v1)
print(v2)

age = 65
num = -1
print(num)
print(age)
r = num+age
print(r)

#if age is put as +65 then pycharm will remove +
#if age is -65 then it will get printed with - sign

#Not operator - its not present in java

is_married = True
print(not is_married) # beacuse of not operator it will print false in output which is opposite of declared variable

#Is Operator - Identity operator
a = 6
b = 6
c = False

print(a is b)

my_list = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list is my_list2) # here output is false because memory location where my_list got store is diff from my_list2's memory location even though the values are same




