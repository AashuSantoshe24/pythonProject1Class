#Method Overloading
#Python doesn't suppor method overloading
#in the traditional sense

class MathUtils(object):

    def add(self, a=0, b=0, c=0):
        return a+b+c

#     def add(self, a, c):
#         return a - c
#
# math = MathUtils()
# op1 = math.add(3,4)
# print(op1)
# op2 = math.add(a=4,b=5,c=7)
# print(op2)

math = MathUtils()
op0 = math.add(7)
op1 = math.add(3,4)
op2 = math.add(3,4, 6)
print(op0)
print(op1)
print(op2)
