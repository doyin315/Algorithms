l=[0,0,1,1,1,2,2,3,3,4]
position=0
for i in range(1,len(l)):
    if l[i]!=l[position]:
        position+=1
        l[position],l[i]=l[i],l[position]
print(position+1)

print(l)
