def repeat(s):
    if len(s)==len(set(s)):
        return True
    return False

s="abcabcbb" 
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if repeat(sub):
            l.append(len(s[i:j]))

print(max(l))
"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def repeat(s):
            if len(s)==len(set(s)):
                return True
            return False 
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub=s[i:j]
                if sub!='' and repeat(sub):
                    l.append(len(s[i:j]))
                    return max(l)
                
        """