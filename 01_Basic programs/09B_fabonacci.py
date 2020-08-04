# Program is to check weather the given no is fabonacci or not
 
# For this perticular problem we have to remember that if (5*n**2+4)or(5*n**2-4)
# is perfect square then a given no is fabonacci num.

import math as M

def perfect_square(x):
    s_root=M.sqrt(x)
    return s_root*s_root == x

def isfabonacci(num):
    return perfect_square((5*(num**2))+4) or perfect_square((5*(num**2))-4)
    
num = int(input())
if isfabonacci(num)==True:
    print("Given number is Fabonacci :)")
else:
    print("Not a Fabonacci number :(")
    
