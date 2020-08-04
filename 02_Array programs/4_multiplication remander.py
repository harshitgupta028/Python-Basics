# Python Program for Find remainder of array multiplication divided by n:

def remainder(arr):
    mul=1
    for i in arr:
        mul=mul*i

    return mul%divider

divider = int(input())
arr = [ 100, 10, 5, 25, 35, 14 ]

print("remainder is:",remainder(arr))    
