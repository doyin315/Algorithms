nums=['990','332','32']
maps=[3,5,4,6,2,7,9,8,0,1]
from collections import defaultdict
def arrange(n,m):
    l=[]
    d=defaultdict(int)
    for i in nums:
        s=''
        for j in i:
            s+=str(maps.index(int(j)))
        d[i]=int(s)
    for i in sorted(d.items(),key=lambda x: x[1]):
        l.append(i[0])
    return l

arrange(nums,maps)

