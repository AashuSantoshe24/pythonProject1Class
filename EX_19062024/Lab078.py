#lambda arguments followed by expression

def find_odd_even(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")


find_odd_even(5)

check_even_odd = lambda num : "Even" if num%2 == 0 else "odd"
print(check_even_odd(11))