score1=int(input("enter the score of the 1st subject: "))
score2=int(input("enter the score of the 2st subject: "))
score3=int(input("enter the score of the 3st subject: "))
score4=int(input("enter the score of the 4st subject: "))
score5=int(input("enter the score of the 5st subject: "))

Average_score=(score1+score2+score3+score4+score5)/5
print(Average_score)
if 90<= Average_score<=100:
    print( "Grage A")
elif 80<=Average_score<=90:
    print("grade B")
elif 70<=Average_score<=80:
    print("grade C")
elif 60<=Average_score<=70:
    print("Grade D")
else:
    print("Grade F")
