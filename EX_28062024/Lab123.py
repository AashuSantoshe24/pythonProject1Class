class Person:
    #class variables or also called as instance variable
    name = "Amit"
    age = None

    def walk(self):

        a = 10 #this is a local variable
        print("I am am Method")
        print("Hi", self.age)

amit = Person()
amit.walk()


