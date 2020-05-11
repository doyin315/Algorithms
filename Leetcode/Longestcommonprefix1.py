s=["flower","flow","flight"]
pref=""
for i in range(len(min(s, key=len))):
    t=set()
    for j in s:
        t.add(j[i])

    if len(t)==1:
        pref+=j[i]
    
    else:
        break

print(pref)
