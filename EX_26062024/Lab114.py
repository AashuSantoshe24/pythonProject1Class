class Person:
    #attributes
    name = None
    id = None
    age = None
    phone_number = None

    #Behaviour
    def talk(self): #this is a normal function, no argument and no return type
        print("I can talk")

    def sleep(self, name): #1 reg, no return
        print("I am a Method!!")
        print("sleep", name)

    def sleep2(self, name): #1 reg, 1 return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): #No arg with return type
        return "I am walking"

#Above program won't give any output

#create Object of the person class
#Object reference = Object --> ClassName()

Surya = Person()
Surya.name = "Surya Prakash"
Surya.talk()

ritika = Person()
ritika.name = "Ritika Gupta"
ritika.walk()