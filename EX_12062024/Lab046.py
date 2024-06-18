#Write a program to calculate and displays the letter
#given numerical score(eg, A B C D or F)
#based on following grade
#input - score - 89
#output 8
#A : 90-100
#B : 80-89 :


#multiple conditions are here sp if elif else

#Step 1 = logic building
#input should be score and its in int
score = int(input("Enter the score"))
#output - string -> A, B, C, D, F -st

#step 2 = wirite the rough logic and convert the real one

#score>=90 and score<=100 then print A
#score>=80 and score<=89 then print B
#score>=70 and score<=79 then print C
#score>=60 and score<=69 then print D
#score>=0 and score<=59 then print F

if score >= 90 and score<=100:
    print("Grade is A")
elif score>=80 and score<=89:
    print("Grade is B")
elif score>=70 and score<=79:
    print("Grade is C")
elif score>=60 and score<=69:
    print("Grade is D")
elif score>=0 and score<=59:
    print("Grade is F")
else:
    print("Invalid score")