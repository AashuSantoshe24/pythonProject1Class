#Reduce line no of earlier code

#earlier program with constructor

class calc:

    #with constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


print(calc(3,4).sum())