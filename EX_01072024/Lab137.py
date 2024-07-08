#multilevel nheritance

class Grandparent:
    key_gold = "1kg"

    def grandparent_method(self):
        return "Grandparent's Method"


class Parent(Grandparent):

    def Parent_method(self):
        return "Parent's Method"


class Child(Parent):
    mac_m3 = "apple M3 Max"

    def child_method(self):
        return "Child's Method"


child = Child()
print(child.grandparent_method())
print((child.Parent_method()))
print(child.child_method())
print(child.key_gold)
print(child.mac_m3)

parent = Parent()
parent.grandparent_method()
print(parent.Parent_method())
print(parent.key_gold)

grandparent_ref = Grandparent()
grandparent_ref.grandparent_method()
grandparent_ref.key_gold
