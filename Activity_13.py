def main():
    a=input_num()
    b=test_prime(a)
def input_num():
    return int(input("enter an integer "))
def test_prime(a):
    if a>1:
        for i in range(2,a):
            if(a%i)!=0:
                print(a,"is a prime number")
                break
            else:
                print(a,"is not a prime number")
                break
        else:
                print(a,"is not a prime number")

main()
        
