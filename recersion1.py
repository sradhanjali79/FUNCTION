def fact(num):
    if num==1:
        return 1
    else:
        return (num*fact(num-1))
x=int(input("enter any number"))
z=(fact(x))
print(z)