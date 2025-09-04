num = int(input("Enter the number : "))
sum = 0
if(num>0):
    for i in range(1,num+1):
        sum = sum+i
else:
    print("Enter integer number...")
    
print("Sum : ",sum)