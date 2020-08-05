def exist(arr,elem):
    
    if elem in arr:
        return True
    
    else:
        return False

lis=list(input().split())        
elem=input()

if exist(lis,elem)== True:
    print("Element found in List :)")
    
else:
    print("Element not found :(")
    