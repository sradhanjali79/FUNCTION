def ng():
    x=int(input("enter number of student"))
    y=int(input("enter money for one student"))
    total_money=x*y
    if total_money<=50000:
        print("Hum budget ke andar hain")
    else:
        print("Hum budget ke bahar hain")
ng()