a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division\n"))
if (c == 1):
    print("sum is ",(a+b))
elif(c == 2):
    print("difference is ",(a-b))
elif(c == 3):
    print("product is ",(a*b))
elif(c == 4):
    print("quotient is ",(a/b))
else:
    print("invalid choice")