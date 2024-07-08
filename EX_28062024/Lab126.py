#Encapsulation : Wrapping/hiding of the data - data binding
#Bind the data variables with the methods
#Data member - class variables
#Methods - Def function within the class
#wrapping or binding the data variables with the methods is also called encapsulation
#Hide the data members (class variables, instance varaibles) by using only the methods

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when a Object is created")

    def change_password(self):
        self.password = "345"
#this is the end of class

xuv = Car()
xuv.password = "345" #this passowrd is now allowed to access outside the class

