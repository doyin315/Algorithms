p=[1,3,1,2,4,2,5,1,8]
piv=p[3]
start=0
end=len(p)-1

for i in range(len(p)):
    if p[i]<piv:
        p[start],p[i]=p[i],p[start]
        start+=1

for i in reversed(range(len(p))):
    if p[i]<piv:
        break

    elif p[i]>piv:
        p[end],p[i]=p[i],p[end]
        end-=1

print(p)