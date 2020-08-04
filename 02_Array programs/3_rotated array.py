# program is for reversing array by given index:

arr=[1,2,3,4,5,6,7,8,9]
rotated_arr=[]

arr_len=len(arr)
index=int(input())
remaning_index=arr_len-index

for i in range(0,remaning_index):
    rotated_arr.append(arr[index+i])
    
for i in range(0,remaning_index+1):
    rotated_arr.append(arr[i])
    
print("Rotated array is:",rotated_arr)    