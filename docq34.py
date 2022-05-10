def list(x):
    i=0
    max1=0
    max2=0
    while i<len(x):
        if x[i]>max1:
            max2=max1
            max1=x[i]
        elif x[i]>max2:
            max2=x[i]
        i=i+1
    print(max1,"+",max2,"=",max1+max2)
list([10, 92, 2, 23, 19])

