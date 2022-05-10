def harshad_num(num):
    sum=0
    x=num
    while num>0:
        sum=sum+(num%10)
        num=num//10
    if x%sum==0:
        return x,("harshad number")
    else:
        return x,("not a harshad number")
def func(y):
    print(harshad_num(y))
func(int(input("enter no.")))
