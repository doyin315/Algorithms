    if not seen.get(i,False):
                seen[i]=True
                backtrack(w,k-1,seen)
                seen[i]=False