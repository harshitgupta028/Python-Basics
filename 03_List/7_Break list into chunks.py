# program for Break a list into chunks of size N
def divide_chunks(l):
    
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
        
l=[1,2,3,4,5,6,7,8,9,4,5,6]
n=5

x=list(divide_chunks(l))
print(x)

# yield - yield is a keyword in Python that is used to return from a function without destroying the states 
# of its local variable and when the function is called, the execution starts from the last yield statement. 
# Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator. 
# yield keyword in Python is less known off but has a greater utility which one can think of.