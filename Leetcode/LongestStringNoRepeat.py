s="abcdbcde"
def lengthOfLongestSubstring(s):
    current=''
    maxNo=0
    for i in range(len(s)):
        if s[i] not in current:
            current+=s[i]
            maxNo=max(maxNo,len(current))    
            print(maxNo)
        else:
            current=current[current.index(s[i])+1:]+s[i]
        print(current)
        

lengthOfLongestSubstring(s)