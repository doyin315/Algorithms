l=[True,False,True,False,False,True]
start=0
for i in range(len(l)):
    if l[i]==False:
        l[i],l[start]=l[start],l[i]
        start+=1

print(l)