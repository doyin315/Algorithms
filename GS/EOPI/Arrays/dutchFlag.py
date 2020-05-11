l=[0,1,2,2,5,1]
piv=l[3]
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[j]<piv:
#             l[i],l[j]=l[j],l[i]

# for i in reversed(range(len(l))):
#     if l[i]<piv:
#         break

    
#     for j in reversed(range(i)):
#         if l[j]>piv:
#             l[j],l[i]=l[i],l[j]
#             break

start = 0
for i in range(len(l)):
    if l[i]<piv:
        l[start],l[i]=l[i],l[start]
        start+=1
end=len(l)-1
for i in reversed(range(len(l))):
    if l[i]<piv:
        break
    if l[i]>piv:
        l[i],l[end]=l[end],l[i]
        end-=1

print(l)


