continue_printing='yes'
while continue_printing=='yes':
    number=int(input("enter the number: "))
    for i in range(1,11):
        print(number, 'x' , i, '=',number*i)
    continue_printing=input("do you want another table enter yes or no: ")
print("Good byee")

    