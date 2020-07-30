# factorial using recursion.

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
print(factorial(int(input())))    

# factorial using loop.

def Factorial(m):
    fact=1
    for i in range(1,m+1):
        fact=fact*i
    return fact
    
print(Factorial(int(input())))        