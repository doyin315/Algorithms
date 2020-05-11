l=[1,3,0]
l[-1]+=1
for i in reversed(range(1,len(l))):
    if l[i]!=10:
        break
    l[i]=0
    l[i-1]+=1

if l[0]==10:
    l[0]=1
    l.append(0)

print(l)