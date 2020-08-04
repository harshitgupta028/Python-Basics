# program is for finding square sum of n natural number

def sq_sum(num):
    sum=0
    for i in range(0,num+1):
        sum=sum+i**2
    return sum
    
print("Square sum of n natural no is:",sq_sum(int(input("Enter any integer:"))))    