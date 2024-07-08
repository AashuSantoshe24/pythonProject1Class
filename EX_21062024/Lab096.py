#decorators

#Its is basically a function which takes another func as an argument and returns a new function that usally extends


def my_decorator(func):
    def wrapper():
        print("Starting your function")
        print("*********")
        func()
        print("*********")
        print("Ending")

    return  wrapper()

@my_decorator
def say_hello():
    print("Say Hello")

