def group(strs):
    store=dict()
    new=[0]*len(strs)
    for i in range(len(strs)):
        new[i]=('').join(sorted(strs[i]))
        
    print(new)
    for i in range(len(new)):
        if not store.get(new[i], False):
            print(new[i])
            store[new[i]]=[strs[i]]
        else:
            store[new[i]]+=[strs[i]]
    
    final=[]
    for i in store.values():
        final.append(i)
    return final
            

s= ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group(s))