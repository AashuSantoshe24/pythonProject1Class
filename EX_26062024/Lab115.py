class Dog:
    name = None #here value is None as it should have some kind of initial value
    id = None

    #Constructor = use to initiate value of instance variable means attributes
    def __init__(self, name, id): #this is how the function is defined
        self.name = name
        self.id = id

    def sleep(self):
        print("sleeping")

dog1 = Dog()
print(dog1.name)
dog1.name = "chow"
print(dog1.name)
dog1.sleep()

dog2 = Dog()
print(dog2.name)
dog2.name = "meow"
print(dog2.name)

