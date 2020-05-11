# l= ["eat", "tea", "tan", "ate", "nat", "bat"]
l=["",""]
seen=dict()
final=[]
for i in range(len(l)):
    if not seen.get(l[i], False) or l[i]=="":
        seen[l[i]]=True 
        res=[]
        res.append(l[i])
        for j in range(i+1,len(l)):
            if  not seen.get(l[j], False) and sorted(l[i])==sorted(l[j]) or l[j]=="" :  
                seen[l[j]]=True
                res.append(l[j])
            print(seen)
        final.append(res)
print(final)
        
