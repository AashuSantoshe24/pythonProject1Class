class Dog:
    name = None #here value is None as it should have some kind of initial value
    id = None

    #Constructor = use to initiate value of instance variable means attributes

    def __init__(self):
        print("Hello")
    def __init__(self, name = None, id = None): #this is how the function is defined
        self.name = name
        self.id = id
        print(self.name)

    def sleep(self):
        print("who is sleeping -->" + self.name)

dog1 = Dog("Chow", "1")
dog2 = Dog("Mow" , "2")
dog3 = Dog()
print(f' {dog1.name} has ID {dog1.id}')
print(f' {dog2.name} has ID {dog2.id}')