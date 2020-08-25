# Program to accept the strings which contains all vowels
def check(string):
    string=string.lower()
    vowel=['a','e','i','o','u']
    s=[]
    for i in string:
        if i in vowel:
            if i not in s:
                s.append(i)

    if len(vowel)==len(s):
        print("Accepted")
    else:
        print("Not Accepted")
        
st="SEEquoaL"
check(st) 
 
    