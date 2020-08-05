def flip(arr):
    
    # fliping first value with last
    index=len(arr)-1
    last_values = arr[index]
    arr[index]=arr[0]
    arr[0]=last_values
    
    return arr 
            
lis=list(map(int, input().split()))     

print(flip(lis))
    