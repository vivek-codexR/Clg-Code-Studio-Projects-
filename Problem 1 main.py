Number = int(input("enet a number :"))
total = 0
print("Table of Given Number:-")
for i in range(1,11):
    
    Table = Number*i
 
    print(Number,"x",i ,"=",Table)
    
    if i%2!=0:
        total = total+Table
print("Total of Alternet numbers=",total)
Square = total**2
print("Square of a number:",Square)
