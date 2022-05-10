def func():
    x =[1, 5, 10, 12, 16, 20]
    y =[1, 2, 10, 13, 16]
    x=x+y
    i=0
    z=[]
    while i<len(x):
        j=0
        while j<len(x):
            if x[i]!=x[j]:
                if x[i] not in z:
                    z.append(x[i])
            j=j+1
        i=i+1
    z.sort()
    print(z)
func()
    
   


        



            