def sub(s):
    def findrange(arr,left,right):
        if left>right:
            return 0
        while (left>=0 and right<len(arr) and arr[left]==arr[right]):
            left-=1
            right+=1
        return right-left-1

    start,end = 0,0
    for i in range(len(s)):
        l1 = findrange(s,i,i)
        l2= findrange(s,i,i+1)
        final=max(l1,l2)
        if final > (end-start):
            start=i-((final-1)//2)
            end=i+(final//2)
    return s[start:end+1]





s='racecar'
print(sub(s))
                    