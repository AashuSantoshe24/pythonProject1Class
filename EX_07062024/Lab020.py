# Strings
# In built Functions
# Function -> Repeat a task - You can use a function
# print(), input, type(), format(), max, min, id(), sum(), avg()

# strings

name = "Amit"
print(name)
print(type(name))
print(id(name))  #id returns idenetity of object where its stored, i.e. memory address
print(len(name)) #length starts from 1 and for Amit its 4

name = name.upper()
print(name)

name = name.casefold()
print(name)

name = name.lower()
print(name)

a = name.count('a')
print(a)

b = name.count('A')
print(b)

print(name[3])  #this represents array

#In python - strigs are immutable - value at particular momery location cant be changed

name[0] = "P" # 'str' object does not suppory item assignment