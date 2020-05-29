def palindrome(s):
    def helper(w,i,j):
        if i>j:
            return 0
        while i<=j and i>=0 and j<len(w) and s[i]==s[j]:
            i-=1
            j+=1

        return j-i-1

    start,end=0,0
    for i in range(len(s)):
        a=helper(s,i,i)
        b=helper(s,i,i+1)
        
        final = max(a,b)
        if final>(end-start):
            end=(final//2)+i
            start=i-((final-1)//2)
        
    return s[start:end+1]

s='madam'
print(palindrome(s))
            
        
print(max('boy','rrrrrrrr'))