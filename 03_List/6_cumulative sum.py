# this program is for Cumulative sum
lis=[10, 20, 30, 40, 50]
cu_lis=[]
cu_lis=[sum(lis[0:i]) for i in range(1,len(lis)+1)]
print(cu_lis)