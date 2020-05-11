"""s='abcdedeara'"""
s='aabbbbaa'
from collections import defaultdict
l=[]
for i in range(1,len(s)):
    count=0
    d=defaultdict(int)
    c=defaultdict(int)
    s1=s[:i]
    s2=s[i:]
    for i in s1:
        d[i]+=1
    for i in s2:
        c[i]+=1
    for i in d:
        if i in c:
            count+=min(d[i],c[i])
        l.append(count)
print(max(l))
            

    