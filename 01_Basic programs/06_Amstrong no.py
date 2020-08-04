# program for checking the no,is Amstrong or not.

lis_of_no=list(map(int, input().split()[0]))
length=len(lis_of_no)
add=0

for i in lis_of_no:
    add=add+(i**length)
    
st= [str(i) for i in lis_of_no]
inp_no = int("".join(st))

if inp_no == add:
    print("Amstrong No.")
else:
    print("Not Amstrong No.")