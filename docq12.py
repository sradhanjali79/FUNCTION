x=["i am shraddha am 18 old",]
i=0
c=0
c1=0
c3=0
while i<len(x):
  print("total length =",len(x[i]))
  j=0
  while j<len(x[i]):
    if x[i][j] in "0,,1,2,3,4,5,6,7,8,9":
      c=c+1
    elif x[i][j]==" ":
      c1=c1+1
    elif ((x[i][j]>="A" and x[i][j]<="Z") or (x[i][j]>="a" and x[i][j]<="z"))and x[i][j]!=" ":
      c3=c3+1
    j=j+1
  i=i+1
print("integer =",c)
print("character =",c3)
print("spaces =",c1)



