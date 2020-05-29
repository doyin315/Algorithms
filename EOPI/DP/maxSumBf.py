# arr=[1,1,3,-2,-2,2,4]
arr=[1,2,3]
count=0
for i in range(len(arr)):
    s=arr[i]
    if i-1!=-1:
        count+=arr[i-1]
    else:
        count=0
    for j in range(i+1,len(arr)):
        s+=arr[j]
        s-=count

        print(s,i,j)

