# program is for sorting first list using second list.
def sort_list(x,y):
    
    zipped=zip(y,x)
    
    z = [x for _, x in sorted(zipped)]
    return z    
        
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] 
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1] 
  
print(sort_list(x, y)) 