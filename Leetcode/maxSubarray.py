l=[1,-1,-1,2]
maxsum=l[0]
cursum=l[0]
for i in range(1,len(l)):
    print(cursum+l[i],l[i])
    cursum=max(cursum+l[i],l[i])
    
    maxsum=max(cursum,maxsum)
    print(maxsum)



