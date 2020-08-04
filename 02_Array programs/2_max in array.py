# program is to find the max number in the array

def largest(arr):
    first_no=arr[0]
    for i in arr:
        if first_no<i:
            first_no=i
            
    return first_no        
    
arr = [25,50,4,85,65]

print("max number of array is:",largest(arr))