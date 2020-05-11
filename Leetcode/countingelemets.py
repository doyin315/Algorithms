l=[1,2,3]
ans=0
seen=dict()
for i in l:
    seen[i]=True
for i in l:
    if seen.get(i+1, False):
        ans+=1
print(ans)
