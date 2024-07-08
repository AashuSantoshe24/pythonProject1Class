class MyClass :
    def __init__(self):
        self.name = "Amit"
        self.email = "xyz@gmail.com"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("This is private, you can only access me via another method")

    def public_fn_private(self):
        self.__private_func()
        print(self.email)

#security = not everyone can access your variables/methods

a = MyClass()
a.public_func()
a.public_fn_private()
