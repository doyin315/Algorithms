arr=[1,2,2,3,4,4,5]
k=0
for i in range(1,len(arr)):
    if arr[i]!=arr[k]:
        k+=1
        arr[k]=arr[i]

print(arr,k)