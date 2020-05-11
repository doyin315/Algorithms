l=[1,2,3,4,5,6,7]
left=0
right=len(l)-1
while left < right:
    if l[left]%2!=0:
        left+=1
    else:
        l[left],l[right]=l[right],l[left]
        right-=1

print(l)

