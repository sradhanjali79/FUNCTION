# def func():
#     l=int(input("enter any number"))
#     x=l
#     sum=0
#     while x>0:
#         sum=sum+(x%10)
#         x=x//10
#     if l%sum==0:
#         print("harshad number")
    
#     else:
#         print("not")
# func()



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
    i=1
    while i<=y:
        print(harshad_num(i))
        i=i+1
func(int(input("enter no.")))





