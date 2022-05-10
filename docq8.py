def str(x):
	i=0
	count=0
	count2=0
	while i<len(x):
		if x[i]>="A" and x[i]<="Z":
			count=count+1
		elif x[i]>="a" and x[i]<="z":
			count2=count2+1
		i=i+1
	print("upper case character",count)
	print("lower case character",count2)
str(input("enter any string"))