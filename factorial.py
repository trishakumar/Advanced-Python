
def fact(n):
    return 1 if(n==1 or n==0) else n*fact(n-1)
n = int(input("enter the number u want to fine the factorial of :"))
print(fact(n))