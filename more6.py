def string_list(x):
    i=0
    z=[]
    while i<len(x):
        if x[i] not in z:
            z.append(x[i])
        i=i+1
    print(z)
string_list(["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"])