def rotated(nums,target):
    i=0
    j=len(nums)-1
    mid=0
    while i<j:
        mid=(i+j)//2
        if nums[mid]>nums[j]:
            i=mid+1
        else:
            j=mid

    offset = i
    i=0
    j=len(nums)-1
    if nums[offset]<=target<=nums[j]:
        while offset<=j:
            mid=(offset+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                offset=mid+1
    else:
        while i<=offset:
            mid=(offset+i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                offset=mid-1
            else:
                i=mid+1
                
    return -1

l=[4,5,6,7,0,1,2]
t=0

print(rotated(l,t))