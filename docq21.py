# num=3
# def func():
#     num=1
#     num = num + 3
#     print(num)

# func()
# print(num)

num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)


