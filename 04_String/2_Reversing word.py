# program for reversing all words in string.

def rever(st):
    Word_lis=st.split(" ")
    return (reversed(Word_lis))

st= "Geeks for Harshit"
print(*rever(st))
