def list(x):
    i=0
    while i<len(x):
        j=0
        max=0
        while j<len(x[i]):
            if x[i][j]>max:
                max=x[i][j]
            j=j+1
        print(max)
        i=i+1
list([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])
