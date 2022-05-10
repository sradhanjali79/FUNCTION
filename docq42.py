def num(x):
    i=0
    z=[]
    while i<len(x):
        sum=0
        while x[i]>0:
            sum=sum+x[i]%10
            x[i]=x[i]//10
        z.append(sum)
        i=i+1
    print(z)
num([12,67,98,34])


