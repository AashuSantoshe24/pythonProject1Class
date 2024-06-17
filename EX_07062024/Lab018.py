#strings
#Bunch of char
# ' ' , " " , " " "

name = 'Harry'
print(name)

name = "Harry"
print(name)

name = """Harry, Is a good person. He love to walk alone, He has a dog
....
....

....
"""
print(name)

#Raw string
dir = r'c:\nomedir\some dir'  #here \n is becoming new line so here we have to add r in this case , r means raw
print(dir)

#Format of the string
first_name = "harry"
last_name = "potter"
print(first_name+ " " + last_name)
print(first_name, last_name)
# f --> formatting - it will replace the values of the variables
# {} --> placeholders
print(f'Your first name is {first_name} {last_name}')