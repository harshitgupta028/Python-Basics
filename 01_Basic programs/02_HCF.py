# Python program to find the HCF of more then two no's

def find_hcf(a,b):
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
    
    hcf = int(gcd)
    return hcf

l = [2, 7, 3, 9, 4] 
a=l[0]
b=l[1]
hcf=find_hcf(a,b)
for i in range(2,len(l)):
    hcf=find_hcf(hcf,l[i])
print(hcf)    
    
