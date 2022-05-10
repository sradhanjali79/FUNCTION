from re import I


def perfect_num(num):
    x=num
    sum=0
    j=1
    while j<num:
        if num%j==0:
            sum=sum+j
        j=j+1
    if x==sum:
        # print(x)
        return x,"is a perfect number"
    else:
        return x,"isn't a perfect number"
def func(y):
    i=1
    while i<=y:
        print(perfect_num(i)) 
        i=i+1
func(int(input("enter any number"))) 
    