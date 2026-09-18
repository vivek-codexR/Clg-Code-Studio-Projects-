account_bal = 0 
Credit_balance = int(input("How much balance you want to deposit ? Please enter your Amount = "))
Account = account_bal + Credit_balance
print("Account Balance =",Account,'Rs.')
Withdraw = int(input("Enter your Withdraw balance ="))
if Withdraw>=100:
    if Withdraw%100==0:
        a = Account - Withdraw
        print("Your withdrawal amount is :", Withdraw,"Rs.")
        print("Now, Your Account Balance is :",a ,"Rs.")
    else:
        print("Please enter an Amount  multiple of x100.")
elif Withdraw<100 and Withdraw>0:
        print("Your account balance is Less than 100Rs. So , Therefore you not able to withdraw this",Withdraw,"Rs.")
else:
    print("Please enter a Positive integer AMOUNT.")

        account_bal = 0 
Credit_balance = int(input("How much balance you want to deposit ? Please enter your Amount = "))
Account = account_bal + Credit_balance
print("Account Balance =",Account,'Rs.')
Withdraw = int(input("Enter your Withdraw balance ="))
if Withdraw>=100:
    if Withdraw%100==0:
        a = Account - Withdraw
        print("Your withdrawal amount is :", Withdraw,"Rs.")
        print("Now, Your Account Balance is :",a ,"Rs.")
    else:
        print("Please enter an Amount  multiple of x100.")
elif Withdraw<100 and Withdraw>0:
        print("Your account balance is Less than 100Rs. So , Therefore you not able to withdraw this",Withdraw,"Rs.")
else:
    print("Please enter a Positive integer AMOUNT.")

        
