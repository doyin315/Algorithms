def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    i=0
    j=len(str(x))-1
    
    while i<j:
        if str(x)[i]!=str(x)[j]:
            return False
        print(i,j)
        x+=1
        j-=1
    
    return True

print(isPalindrome(121))
    