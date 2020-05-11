s=list({1,7,2,4})
d=[]
solution=set()
for i in range(len(s)):
    for j in range(len(s)-1,i,-1):
        if s[i]+s[j] not in d:
            d.append(s[i]+s[j])
        else:
            continue
for i in range(len(d)):
    for j in range(len(d)-1,i,-1):
        if (d[i]+d[j])%3!=0:
            solution.add(d[i])
            solution.add(d[j])