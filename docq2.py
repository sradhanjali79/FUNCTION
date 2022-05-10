def list(x):
	i=0
	max3=0
	max2=0
	max1=0
	while i<len(x):
		if x[i]>max1:
			max3=max2
			max2=max1
			max1=x[i]
		elif x[i]>max2:
			max2=x[i]
		elif x[i]>max3:
			max3=x[i]
		i=i+1
	print(max1,"is first maximum")
	print(max2,"is second maximun")
	print(max3,"is third maximum")
list([2,4,3,9,7,6])
