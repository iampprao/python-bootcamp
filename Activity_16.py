def input_string():
    a=input("Enter string  here ")
    return a
def tup(a):
    b=list()
    for i in a.split(';'):
        c=i.split('=')
        b.append(tuple(c))
    return b
y=input_string()
x=tup(y)
print(x)
