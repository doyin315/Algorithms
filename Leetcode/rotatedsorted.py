def rotate(arr,t):
    i=0
    j=len(arr)-1

    while i<j:
        mid=(i+j)//2
        if arr[mid]> arr[j]:
            i=mid+1
        else:
            j=mid

    offset=i
    i=0
    j=len(arr)-1

    if t>=arr[offset]and t<arr[j]:
        while offset<j:
            mid=(offset+j)//2
            if arr[mid]==t:
                return mid
            elif arr[mid]>t:
                j=mid
            else:
                offset=mid+1
    else:
        while i<offset:
            mid= (offset+i)//2
            if arr[mid]==t:
                return mid
            elif arr[mid]>t:
                offset=mid
            else:
                i=mid+1

l=[5,6,7,1,2,3,4]
print(rotate(l,3))

    