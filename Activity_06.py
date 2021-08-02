a = input('enter the elements')
b = a.split()
l=list(b)
print(l)
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
