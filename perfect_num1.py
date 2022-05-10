def perfect_num(num):
    x=num
    sum=0
    j=1
    while j<num:
        if num%j==0:
            sum=sum+j
        j=j+1
    if x==sum:
        return x,"is a perfect number"
    else:
        return x,"isn't a perfect number"
def func(y):
        print(perfect_num(y)) 
func(int(input("enter any number")))