Hindi = int(input("Enter a number of Hindi Sub. :"))
English = int(input("Enter a number of English Sub. :"))
Maths = int(input("Enter a number of maths Sub. :"))
Physics = int(input("Enter a number of Physics Sub. :"))
Chemistry = int(input("Enter a number of Chemistry Sub. :"))
Total_number = (Hindi+English+Maths+Physics+Chemistry )/5
if Hindi>=33 and English>=33 and Maths>=33 and Physics>=33  and Chemistry>=33:
    if Total_number>=85:
        print("Pass with Grade A+ and Total number of percentage is:",Total_number,"%")
    elif Total_number>=65:
        print("Pass with Grade B and Total number of percentage  is:",Total_number,"%")
    elif Total_number>=45:
        print("Pass with Grade C and Total number of percentage is:",Total_number, "%")
    elif Total_number>=33:
        print("Pass with Grade D and Total number of percentage is:",Total_number,"%")
else:
    print("You are Fail. ")
