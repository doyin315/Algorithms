def find(l,t,s=[]):
    if len(l)==0:
        return [-1,-1]
    i=0
    j=len(l)-1
    while i<=j:
        mid=(i+j)//2
        if l[mid]==t:
            break
        elif l[mid]>t:
            j=mid-1
        else:
            i=mid+1
    if l[mid] != t:
        return [-1,-1]       

    left=mid-1
    count=0
    while left>=0:
        if l[left]==t:
            count+=1
            left-=1
        else:
            break
    left=mid-count
    count=0
    right=mid+1
  
    while right<len(l):
        if l[right]==t:
            count+=1
            right+=1
        else:
            break
    right=mid+count

    return [left,right]

l=[1,4]
t=4

print(find(l,t))


