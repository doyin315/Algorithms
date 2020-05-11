arr=['aba','baba','aba','xzxb']
q=['aba','xzxb','ab']
l=[0]*len(q)
for i in range(len(q)):
    for j in range(len(arr)):
        if q[i] == arr[j]:
            l[i]+=1
print(l)