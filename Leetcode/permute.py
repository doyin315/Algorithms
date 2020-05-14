def permute(nums):
    res=[]
    def backtrack(s=[],current=-1,seen={}):
        if current>=0:
            seen[current]=True
            s.append(nums[current])
        
        if len(s)==len(nums):
            res.append(s[:])
        else:
            for i in range(len(nums)):
                if not seen.get(i,False):
                    backtrack(s,i,seen)
                    s.pop()
                    seen[i]=False
    backtrack()      
    print(res)




l=[1,2,3]
permute(l)
