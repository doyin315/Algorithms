def balance(arr):
    right=0
    left=0
    s=sum(arr)
    mid=s//2
    for i in arr:
        right+=i
        if right>=mid:
            left=right-i
            right=0
    if left==right:
        return True
    return False
a=[1,6,3,5,2]
print(balance(a))

