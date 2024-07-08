print("--Start of the program--")
try:
#code of whatever we want to do
    a = int(input("enter the num1"))
    b = int(input("enter the num2"))
    c = a / b
    print("Result Div is", c)
except Exception as e:
    print(e)
    print("Please enter integer!")

print("-- End if the Program ---")