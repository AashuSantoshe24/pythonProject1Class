#Same program with user inputs

class Student:

    def __init__(self):
        self.name = input("Enter the name")
        self.age = input("Enter the age")

    def display(self):
        print(f"Name is {self.name}, Age is {self.age}")

Student1 = Student()
Student1.display()