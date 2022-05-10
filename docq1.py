def name():
	list=["abc","xyz","aba","1221"]
	i=0
	count=0
	while i<len(list):
		if list[i][0]==list[i][-1]:
			count=count+1
		i=i+1
	print(count)
name()