n = input("Enter the string \n")

vowels = 0
consonents = 0
for i in n:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels = vowels + 1
    else:
        consonents = consonents + 1

print("The no of vowels are", vowels)
print("The no of consonents are", consonents)
