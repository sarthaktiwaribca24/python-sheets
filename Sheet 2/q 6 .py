a = int(input("Enter the number : "))
sum = 0
for i in range(1,a):
    if(i%2==0):
        sum = sum+i
        
print("Sum of even no : ",sum,end=" ")