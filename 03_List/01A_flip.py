def flip(arr,pos1,pos2):
    
    # fliping first value with last
    first_pos = arr[pos1]
    arr[pos1]=arr[pos2]
    arr[pos2]=first_pos
    
    return arr 
            
lis=list(map(int, input().split()))
pos1 = int(input())
pos2 = int(input())

print(flip(lis,pos1,pos2))
    