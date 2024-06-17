#Take 2 int nos from user and we want to add them
#we need to use the input() function

num1 = input("enter 1st no : ")
num2 = input("enter 2nd no : ")

#result = num1+num2
#print(result)


#above is concatinating string so now type conversion - str ->int -> ? int()

result = int(num1)+int(num2)
print(result)

# + --> int sum operation
# + --> str - concat
#int to str --> str()
#str to int --> int()

print(type(int(num1)))