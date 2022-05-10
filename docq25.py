# def int(x):
x=[2,-7,64,-6,-7,8]
i=0
count=0
count1=0
while i<len(x):
    if x[i]>0:
        count+=1
    else:
        count1+=1
    i+=1
print("posituve integer",count)
print("negative integer",count1)
# int([2,-7,64,-6,-7,8])