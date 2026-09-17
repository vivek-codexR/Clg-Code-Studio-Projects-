TOtal_Units = int(input("Enter your net units ="))
if TOtal_Units<=100 and TOtal_Units>0:
        A = TOtal_Units*5
        print("Your Total bill is = ",A,"Rs.")
elif TOtal_Units>100 and TOtal_Units<=200:
        A = TOtal_Units*7
        print("Your Total bill is = ",A,"Rs.")
elif TOtal_Units>200:
        A = TOtal_Units*10
        print("Your Total bill is = ",A,"Rs.")   
else:
    print("invailed syntax , please enter a Postive integer units.")
        
