#try, except and finally

try:
    num1 = int(input("Enter a number 1\n"))
    num2 = int(input("Enter a number 2\n"))
    result = num1/num2
    print(result)
except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'Result is {result}')
finally:
    print("I will be executed anyhow!!")