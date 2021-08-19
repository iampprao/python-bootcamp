import math
degree=float(input("input in degrees: "))
pi=22/7
x=degree*(pi/180)
sinx=x**1/math.factorial(1)-x**3/math.factorial(3)+x**5/math.factorial(5)-x**7/math.factorial(7)+x**9/math.factorial(9)
print("the sine of the given angle is ",sinx)

