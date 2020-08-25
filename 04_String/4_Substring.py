# python program to find the sub string in a main string.

def substring(s1,s2):
    if s1.find(s2)==-1: 
        print(False)
    else: 
        print(True)
        
s1 = "geeks for geeks"
s2 = "gee"
substring(s1,s2)