l=[3,3,5,0,0,3,1,4]
minfar=l[0]
profit=0
res=[0]*len(l)
res1=[0]*len(l)
pos=0
for i in range(1,len(l)):
    minfar=min(minfar,l[i])
    profit=max(profit,l[i]-minfar)
    res[i]=profit
print(res)
maxfar=l[-1]
profit=0
for i in reversed(range(len(l)-1)):
    maxfar=max(maxfar,l[i])
    profit=max(profit,maxfar-l[i])
    res1[i]=profit
print(res1)


for i in range(1,len(res1)):
    res1[i]+=res[i-1]
print(res1)








