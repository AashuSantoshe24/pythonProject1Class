#leed code program for sum of digits

number = 12345
sum_of_digits = 1+2+3+4+5

#if you keep diving 12345 by 10 then i=at first it will give 5 as reminder then 4 as reminder then 3, 2 and

n1 = 12345/10
print(n1) #1234.5

r1 = number%10
q1 = number//10
print(r1)
print(q1)

r2=q1%10
q2=q1//10
print(r2)
print(q2)

r3=q2%10
q3=q2//10
print(r3)
print(q3)

r4=q3%10 #reminder
q4=q3//10 #quotient
print(r4)
print(q4)

r5=q4%10
q5=q4//10
print(r5)
print(q5)

print(r1+r2+r3+r4+r5)

def sum_of_digits(number):
    #Base case
    if number < 10:
        return number
    #recursive case
    else:
        return number%10 + sum_of_digits(number//10)

print(sum_of_digits(12345))

