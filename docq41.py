def list(x):
    i=0
    z=[]
    while i<len(x):
        j=0
        count=0
        while j<len(x[i]):
            if x[i][j] in x[i]:
                count=count+1
            j=j+1
        z.append(count)
        i=i+1
    k=0
    max=0
    min=z[0]
    while k<len(z):
        if z[k]>max:
            max=z[k]
        elif z[k]<min:
            min=z[k]
        k=k+1
    p=z.index(max)
    q=z.index(min)
    print((max,x[p]))
    print((min,x[q]))
    

list([[1,2], [3],[1, 3], [5, 7], [9, 11], [13, 15, 17],[2,7,9,110]])
        