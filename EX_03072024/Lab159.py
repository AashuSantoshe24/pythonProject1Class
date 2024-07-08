#File IO

#File IO
try:
    file = open('pramod.txt', 'r'):
        print(file.read())
        file.close()
except FileNotFoundError as fnfe:
    print("I am not able to find the file , please")
else:
    print("closing the file")
finally:
    file.close() #close has to be executed