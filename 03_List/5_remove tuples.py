# program is for removing empty tupple.

def Remove(tuples): 
    tu=[]
    for t in tuples:
        if t:
            tu.append(t)
    return tu 
  
# Driver Code 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
print(Remove(tuples)) 
