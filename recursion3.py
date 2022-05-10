def str(x,y):
    if y==0:
        print(x[0])
    else:
        print(x[y],end="")
        str(x,y-1)
x=input("enter string ")
str(x,len(x)-1)
