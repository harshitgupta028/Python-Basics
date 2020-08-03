# python program to find the n'th fabonic no.

# BAsic thing while calculating nth fabonic series no. is 

# F(n) = F(n-1)+F(n-2)

def fabonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)
        
print(fabonacci(int(input("nth fabonacci no is: "))))
        