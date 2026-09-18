b = 0
count = 0
for i in range (7):
    a = int(input("enter a data by day:"))
    b = b+a
    
    if a>2:
        count +=1
print("Total GB =",b)
print("Total day = ",count)
    
