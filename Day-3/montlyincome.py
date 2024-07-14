montly_income=int(input("enter the income amount: "))
rent=int(input("enter the rent amount: "))
groceries=int(input("enter the groceries amount: "))
utilities=int(input("enter the utilities amount: "))
entertainment=int(input("enter the entertainment amout:"))
total_expenses=rent+groceries+utilities+entertainment

remaining_amount=montly_income-total_expenses

if remaining_amount>0:
    print("you are within your budget")
else:
    print("you are not within your budget")