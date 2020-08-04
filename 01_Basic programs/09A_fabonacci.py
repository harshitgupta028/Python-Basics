# Program to print all fabonacci no

start = 0
mid = 1
end = 100
c=0
for i in range(start,end):
    start = mid 
    mid = c
    print(c,end=" ")
    c = start + mid