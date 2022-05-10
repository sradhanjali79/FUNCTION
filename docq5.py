def list(x):
	i=0
	z=[]
	while i<len(x):
		if x[i] not in z:
			z.append(x[i])
		i=i+1
	print(z)
list([1,2,3,3,3,4,3,5])