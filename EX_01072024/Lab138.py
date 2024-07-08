#multiple inheritance

class Father:

    def father_money(self):
        return

    def home(self):
        return "This is from Father"

class Mother:

    def mother_money(self):
        return "2"

    def home(self):
        return "This is from Mother"

class Son(Father, Mother): #method resolution
    pass

son = Son()
son.father_money()
son.mother_money()
print(son.home()) #Here both Father and Mother class has Home function so which function will call here? Its the one which is mentioned first in Son class at line no 22

