l=[2,3,5,5,7,7,7,1,1,17,13]
write_index=1
print(l)
for i in range(1,len(l)):
    if l[i]!=l[i-1]:
        l[write_index]=l[i]
        write_index+=1
print(write_index)