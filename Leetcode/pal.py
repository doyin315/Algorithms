def palindromeSearch(word,k):
  seen=dict()
  found=[False]
  def helper(s,removed):
    i=0
    j=len(s)-1
    
    while i<=j:
      if removed.get(i, False):
        i+=1
      if removed.get(j, False):
        j-=1
        
      if s[i]!=s[j]:
         return False
      i+=1
      j-=1
    return True
  
  def backtrack(w,k,seen):
    if k<=0:
      pass
    
    else:
      if helper(w,seen):
        found[0]=True
        print('yeh')
      else:
        for i in range(len(word)):
            if not seen.get(i,False):
                seen[i]=True
                # print(seen)
                backtrack(w,k-1,seen)
                seen[i]=False

  backtrack(word,k,seen)
  return found[0]
  
print(palindromeSearch('ragcecarf',2))



# def palindromeSearch(word,k):
#   seen=dict()
#   found=[False]
#   def helper(s,removed):
#     i=0
#     j=len(s)-1
    
#     while i<=j:
#       if removed.get(i, False):
#         i+=1
#       if removed.get(j, False):
#         j-=1
#       if i>j:
#         return False
      
#       if s[i]!=s[j]:
#          return False
#       i+=1
#       j-=1
#     return True
  
#   def backtrack(w,k,seen):
#     if k<=0:
#       pass
    
#     else:
#       if helper(w,seen):
#         found[0]=True
#       else:
#         for i in range(len(word)):
#           if not seen.get(i,False):
#             seen[i]=True
#             backtrack(w,k-1,seen)
#             seen[i]=False

#   backtrack(word,k,seen)
#   return found[0]
  

