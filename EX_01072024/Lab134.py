#Inheritance : aquire attributes and behaviour, Data members and methods

#suppose my father has 3BHK house - Ingeritance - son

#Concepts of OOPS
#that allows a class(child class) to i herit attributes and methods
#from another class




class Grandparent : #This is parent/base class
    key = "abv@123"
    def grandparent_method(self):
        return "Grandparent's method"

class Father(Grandparent): #This is child class/sub class

    def parent_method(self):
        return "Parent's method"


grandfather = Grandparent()
grandfather.grandparent_method()
# grandfather.parent_method() # grandfather can't call parent method

parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)