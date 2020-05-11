s=["flower","flow","flight"]
def longestpref(strs):
    prefix=""
    count=0
    p=[]
    for i in range(len(min(strs, key=len))):
        for j in strs:
            p.append(j[count])
  
        if len(set(p))==1:
            prefix+=p[0]
        elif not p:
            return ""
        else:
            return prefix
        count+=1
        p=[]
        
    return prefix
            
            
print(longestpref(s))