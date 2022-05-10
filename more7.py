def func():
    x = [1, 342, 75, 23, 98]
    y = [75, 23, 98, 12, 78, 10, 1]
    x=x+y
    i=0
    z=[]
    while i<len(x):
        j=0
        while j<len(y):
            if x[i]!=y[j]:
                if x[i] not in z:
                    z.append(x[i])
            j=j+1
        i=i+1
    print(z)
func()


    


