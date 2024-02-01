x=int(input('enter num1: '))
y=int(input('enter num2: '))
z=int(input('enter num3: '))

if x>=y:
    if(x>=z):
        print(x, 'is the largest')
    else:
        print(z, 'is the largest')
elif y>=x:
    if(y>=z):
        print(y, 'is the largest')
    else:
        print(z, 'is the largest')
else:
    print(z,'is the largest')
