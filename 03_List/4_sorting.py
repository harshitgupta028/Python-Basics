# program for finding second largest no in list

lis = [5,4,3,1,8,6]

maximum = max(lis[0],lis[1])
second_max = min(lis[0],lis[1])

for i in range(2,len(lis)):
    if lis[i]>maximum:
        second_max=maximum
        maximum=lis[i]
        
    elif lis[i]>second_max and maximum!=lis[i]:
        second_max=lis[i]
        
    else:
        if maximum==second_max:
            second_max=lis[i]
print("Second maximum in the list is:", second_max)