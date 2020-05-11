d=['A','B','C']
s=[0,0,0]
fin=[]
l=[25,8,2,35,15,120,55,42]
for i in l:
    index=s.index(min(s))
    s[index]+=i
    fin.append(d[index])
print(fin)
