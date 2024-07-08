# where earlier 096 is used ?
import time


def note_time_decorator(func):
    def wrapper(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time Taken" + (end_time - start_time))

    return wrapper

@note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the log of time taken")


