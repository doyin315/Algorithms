
def isPalindrome(t): 
  
    # Run loop from 0 to len/2  
    for i in range(0, len(t)//2):  
        if t[i] != t[len(t)-i-1]: 
            return False
    return True


s='tacocat'
l=[]
def is_palindrome(t):
    return t==t[-1::-1]
count=len(s)
for i in range(len(s)):
    for j in range(i+2,len(s)+1):
            print(s[i:j])
            if isPalindrome(s[i:j]):
                count+=1
print(count)