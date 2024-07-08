#Hybrid Inheritanec
#Its a combination of multiple and multilevel

class A:

    def methodA(self):
        return "Method A"

class B(A):

    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"

class D(B, C): #multiple and multilevel

    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
