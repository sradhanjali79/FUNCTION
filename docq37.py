def bool(x):
    i=0
    count=0
    while i<len(x):
        if x[i]==True:
            count=count+1
        i=i+1
    print(count)
bool([True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True])