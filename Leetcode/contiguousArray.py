arr=[1,1,0,0,0,1,1,1]
d=dict()
one=0
zero=0
count=0
res=[]
start=0
d[count]=0
for i in range(len(arr)):
    if arr[i]==0:
        count-=1
    else:
        count+=1

    if count in d.keys():
        
        res.append((d[count],i))
    print(count,i)
    d[count]=i

print(res)
