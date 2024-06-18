#How to check multiple condition

# problem to find max between 3 nos

#num1, num2, num3

#num1>num2 and num1>num3 then num1 is greater
#num2>num1 and num2>num3 then num2 is greater
#if above 2 conditions are false then num 3 is greater

num1 = int(input("Enter the no one"))
num2 = int(input("Enter the no two"))
num3 = int(input("Enter the no three"))

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


#Or use max function like below
result = max(num1, num2, num3)
print(result)