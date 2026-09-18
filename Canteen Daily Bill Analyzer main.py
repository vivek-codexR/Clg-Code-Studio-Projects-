while True:
    Food_Menu = """
          ____________________
          | "Pizza =150rs."   |
          | "Burger = 100Rs." |
          | "Coldrink = 60Rs."|
          |___________________|
          
{ If you buy a 500Rs. plus amount of 'PIZZA'  ,  'Burger'  ,  'Coldrink' or "ALL Foods" then you must gain 10% discount in Bill Amount.}
    =} Big Note for All Food :- If You buy a *Total Bill\All Foods  Amount >1200Rs. , then you must gain a 20% discount in final or total bill. """
    A = input("\nToo check the Food Menu, Please Enter a ' Menu' :")
    while  A.lower() != "menu":
        print("WRONG!!!\nPlease enter only 'Menu:")
        A = input("\nToo check the Food Menu, Please Enter a ' Menu' :")

    print("-:\n\n Food_Menu:-",Food_Menu) 
   

    Pizza = 150
    Burger = 100
    Colddrink = 60
    Choice = input("\n\nWhich food you want ?\nPlease enter here : ")

    if Choice == "Pizza" or Choice == "pizza" or Choice == "PIZZA":

        Quantity1 = int(input("How much number of Pizza: "))

    elif Choice == "burger" or Choice == "Burger" or Choice == "BURGER":

        Quantity2 = int(input("How much number of Burger: "))

    elif Choice == "COLDRINK" or Choice == "coldrink" or Choice == "Coldrink":

        Quantity3 = int(input("How much number of Colddrink: "))

    else:

        Quantity1 = int(input("How much number of Pizza: "))
        Quantity2 = int(input("How much number of Burger: "))
        Quantity3 = int(input("How much number of Colddrink: "))

         
    print ( """-: Food Code :-
   
 1 Pizza: 
     
 2 Burger:

 3 Colddrink:

 4 All Food:
     _______________*_*_*_*_*_*_*_*_*_*_*_______________""")

    Choice = int ( input ( "\nEnter a Food Code:" ) )

    if Choice== 1:
          if  Pizza*Quantity1 >500: 
              B =   (Pizza*Quantity1)*10/100
              Bill = Pizza*Quantity1-B
              print ("Your Bill of Foods:",Bill, "Rs.")
          else:
                   print ("Your Bill of Foods:", Pizza*Quantity1, "Rs.")
     

    elif Choice== 2:
         if  Burger*Quantity2 >500: 
              B =   (Burger*Quantity2)*10/100
              Bill = Burger*Quantity2-B
              print ("Your Bill of Foods:",Bill, "Rs.")
         else:
                  print ("Your Bill of Foods:", Burger*Quantity2, "Rs.")
    elif Choice== 3:
          if  Colddrink*Quantity3 >500: 
             B =   (Colddrink*Quantity3)*10/100
             Bill = Colddrink*Quantity3-B
             print ("Your Bill of Foods:",Bill, "Rs.")
          else:
                  print ( "Your Bill of Foods:", Colddrink*Quantity3, "Rs.")

    elif Choice== 4:

           TOTAL_bill = Pizza*Quantity1 +Burger*Quantity2+Colddrink*Quantity3
           if   TOTAL_bill >500 and  TOTAL_bill<1200: 
              B =   ( TOTAL_bill)*10/100
              Bill =  TOTAL_bill-B
              print ("Your Bill of Foods:",Bill, "Rs.")
           elif  TOTAL_bill >=1200: 
                 B =   ( TOTAL_bill)*20/100
                 Bill =  TOTAL_bill-B
                 print ("Your Bill of Foods:",Bill, "Rs.")     
           else:
                    print ( "Total Bill of Foods:", TOTAL_bill, "Rs. ")
    else:

        print ( "WRONG !!! FOOD CODE , Food Not Available")
