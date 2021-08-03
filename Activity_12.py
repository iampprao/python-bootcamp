a=input()
b=a.split()
z=list(b)
p=int(z[0])
q=int(z[1])
r=int(z[2])
if(p>=q)and (p>=r):
    x=p
elif(q>=p) and (q>=r):
    x=q
else:
    x=r
print("%d is the greatest number among %d %d %d" %(x,p,q,r))
