#Recursion
#its a programming technique where a function calls itself to solve a problem
# def factorial(n):
#     """
#     Recursively calculates the factorial of a number
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

#key concept : In case of recursion then you have to divide concept in Base case and recursive case

#Factorial

#Recursive case will run until we reach base case
def factorial(n):

    #Base case
    if n == 0 or n == 1:
        return 1
    #recursive case
    else:
        return n * factorial(n-1)


print(factorial(5))