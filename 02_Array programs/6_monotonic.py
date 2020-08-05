# Program for checking monotonic Array or Not

# for monotonic we need to know that what is monotonic
# for monotonic A[i]<=A[i+1] or A[i]>=A[i+1]

def monotonic(arr):
    
    return (all(arr[i]<=arr[i+1] for i in range(0,len(arr)-1)) or 
            all(arr[i]>=arr[i+1] for i in range(0,len(arr)-1)))
            
lis=list(map(int, input().split()))     

if monotonic(lis)==True:
    print("This array is monotonic")

else:    
    print("This array is not monotonic")