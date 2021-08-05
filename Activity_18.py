def main():
    a=input_string()
    b=tup(a)
    display(b)
def input_string():
    return input("Enter a String: ")
def tup(a):
    b=list()
    for i in a.split(';'):
        c=i.split('=')
        b.append(tuple(c))
    return b
def display(b):
    print(dict(b))
main()
