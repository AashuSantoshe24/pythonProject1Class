
def outer_function():
    var1 = 30

    def inner_function(): # def of inner funct
        print(var1)
    inner_function() #calling for inner function

outer_function() #calling for outer func

#python interpreterer will see 1st their is a out ter function with var in side it , then it will see that their is inner function to print var so we have to irst call inner function then outer to print otherwise it won't get printed