#Program to find max between two nos

a = int(input("Enter no 1"))
b = int(input("Enter no 2"))

#max

result = max(a,b)
print(result)

#or we can use below logic if we dont want to use above max function

if a>b:
    print(a)
else:
    print(b)