# def prime(limit):
#     i=0
#     while i<=limit:
#         j=1
#         count=0
#         while j<=i:
#             if i%j==0:
#                 count+=1
#             j+=1
#         if count==2:
#             print(i)
#         i+=1
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
        return n
        pass
def func(y):
    i=1
    while i<=y:
        print(prime_num(i))
        i=i+1
func(int(input("enter any number")))