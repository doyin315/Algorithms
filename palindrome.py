def ispalindrome(s):
    s=s.replace(" ","")
    return s==s[-1::-1]
    

def ispalindrome1(s):
    new_s=""
    for i in s:
        if i!=" ":
            new_s+=i
    reversed_s=""
    for j in range(len(new_s)-1,-1,-1):
        reversed_s+=new_s[j]
    return new_s==reversed_s


    


t="hwll"
print(ispalindrome1(t))

