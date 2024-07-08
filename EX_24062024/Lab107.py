numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def doubler(number):
    return number * 2

def even_giver(n):
    return n%2 == 0

doubled_numbers = map(doubler, numbers)
even_numbers = filter(even_giver, numbers)
print(list(doubled_numbers))
print(list(even_numbers))