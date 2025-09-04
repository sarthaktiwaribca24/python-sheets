num = int(input("Enter the number : "))

if(num>0):
    for i in range(num,0,-1):
        print(i,end=" ")
else:
    print("Enter integer number...")