number1 = int(input("Enter a number: "))
number2= int(input("Enter a number: ")) 
number3 = int(input("Enter a number: "))

if( number1 > number2 and number1 > number3):
    print("number1 is greater")
    if( number2 > number1 and number2 > number3):
        print("number2 is greater")
else:
    print("number3 is greater5")