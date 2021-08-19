def main():
    y={}
    n=inpnum()
    for i in range(n):
        key=input("Enter key :")
        value = input("Enter value :")
        y[key]=value
    print("Before sorting - ",y)
    
    dict1 = sorted(y.items())
    print("After sorting - ",dict(dict1))


def inpnum():
    n=int(input("Enter the number of elements in the dictionary - "))
    return n

main()
