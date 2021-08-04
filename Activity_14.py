def take_input():
    l=int(input("enter the lenght: "))
    b=int(input("enter the breadth: "))
    h=int(input("enter the height: "))
    return l,b,h
def volume(l,b,h):
    k=(l**2)+(b**2)+(h**2)
    vol=(b**2)*(h**2)/(k**(1/2))
    return vol
def display(vol):
    print("volume of tromboloid is %.3f" %vol)
def main():
    l,b,h=take_input()
    vol=volume(l,b,h)
    display(vol)

main()
