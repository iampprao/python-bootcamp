a = input('enter the elements')
b = a.split()
for i in range(0,len(y)):
  b[i]=int(b[i])
c=b[0:3]
print("sliced list= ",c)
b[0]=0
b[-1]=0
print("replace list1= ",b)
c[0]=0
c[-1]=0
print("replace list2= ",c)
r=l[::-1]
print("reversed list= ",r)
