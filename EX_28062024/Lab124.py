class Car:
    make = None
    name = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.make = o_make
        self.name = o_name
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name" + self.name)
        print("Starting a car with the make" + self.make)
        print("Starting a car with the model" + self.model)
#This is the end of class

lambo = Car(o_name="lambo", o_make="V2", o_model="2024")
lambo.start_engine()

xuv = Car(o_name="XUV", o_make="V6", o_model="2023")
xuv.start_engine()