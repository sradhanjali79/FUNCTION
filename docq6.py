def even(x):
	i=0
	z=[]
	while i<len(x):
		if x[i]%2==0:
			if x[i] not in z:
				z.append(x[i])
		i=i+1
	print(z)
even([1,2,3,4,5,6,7,8,9])