def wsearch(arr,word):
    def dfs(x,y,arr,seen,index,word,stack):
        if index==len(word):
            return True

        seen[(x,y)]=True
        for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
            if arr[x1][y1]==word[index] and 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False):
                stack.append((x1,y1))
                print(stack)
                if dfs(x1,y1,arr,seen,index+1,word,stack):
                    return True
                stack.pop()

        return False
    d=dict()
    stack=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==word[0]:
                d[(i,j)]=True
                if dfs(i,j,arr,d,1,word,stack):
                    return True
    return False

    
arr=[['A','E','D','T'],
    ['W','E','D','P'],
    ['E','M','L','O']]
w='AEDM'

print(wsearch(arr,w))