# def prime(x):
#     i=1
#     count=0
#     while i<=x:
#         if x%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print(x,"is a prime number")
#     else:
#         print(x,"is a composite number")
# prime(int(input("enter any number"))) 

def prime_num(num):
    count=0
    n=num
    j=1
    while j<=num:
        if num%j==0:
            count=count+1
        j=j+1
    if count==2:
        return n,"is a prime number"
    else:
        return n,("is a composite number")
def func(y):
    print(prime_num(y))
func(int(input("enter any number")))
