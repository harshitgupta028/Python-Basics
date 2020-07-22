# Python program to find the LCM of more then two no's
def find_lcm(a,b):
    if a>b:
        num=a
        den=b
    else:
        num=b
        den=a
    rem=num%den
    
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    gcd=den    
    
    lcm= int(int(a*b)/int(gcd))    
    return lcm

l = [2, 7, 3, 9, 4] 

a=l[0]
b=l[1]

lcm=find_lcm(a,b)

for i in range(2,len(l)):
    lcm=find_lcm(lcm,l[i])
print(lcm)    
    
