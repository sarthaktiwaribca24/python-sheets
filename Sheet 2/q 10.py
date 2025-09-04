num = 12321
rev=0

for i in range(num):
    if(num>0):
        temp = num%10
        rev = rev*10+temp
        num = num//10
    if(num==rev):
            print("yes")