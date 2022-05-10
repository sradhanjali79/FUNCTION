def max():
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    z=int(input("enter third number"))
    if x>y and x>z:
        print(x,"is greater")
    elif y>x and y>z:
        print(y,"is greater")
    elif z>x and z>y:
        print(z,"is greater")
max()