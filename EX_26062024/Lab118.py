class calc:

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    #with constructor
    def __init__(self):
        print("Hello DC")


object_ref = calc()
output = object_ref.sum(3,4)
print(output)