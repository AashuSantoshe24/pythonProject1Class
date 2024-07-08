class Car:
    name = None

    def __init__(self):
        self.public_var = "public" #
        self._protected_var = "Protected123" #this is available to access within the module
        self.__private_var = "pass@123" #private things are allowed to access in class

    def __private_method(self):
        print("protected!")

    def printName(self):
        self.__private_method()
        print("I am allowed public")
        if self.__private_var == "123":
            print("hi, 123")
        print("I am allowed public")
#this is end of the class

alto = Car()
alto.public_var = "hahaha" #this is not a secure class as I am able to access it outside the class

