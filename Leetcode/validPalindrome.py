def isPalindrome(s):
    if not s:
        return True
    s=s.lower()
    i=0
    j=len(s)-1
    
    while i<=j:
        if s[i].isalnum() and s[j].isalnum():
            print(s[i],s[j])
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        elif s[i].isalnum():
            j-=1
        else:
            i+=1
            
    return True
l="A man, a plan, a canal: Panama"

print(isPalindrome(l))