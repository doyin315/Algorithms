count=0
def connected(arr):
    maxcounter=0
    def dfs(arr,x,y,stack,seen):
        global count
        for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
            if 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False) and arr[x1][y1]==1:
                count+=1
                seen[(x1,y1)]=True
                stack.append((x1,y1))
                dfs(arr,x1,y1,stack,seen)
                stack.pop()
    global count
    stack=[]
    seen=dict()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==1 and not seen.get((i,j),False):
                count=0
                seen[(i,j)]=True
                count+=1
                dfs(arr,i,j,stack,seen)
                maxcounter=max(maxcounter,count)
    print(maxcounter)
    return maxcounter





arr1=[[1,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,0]]
arr2=[[1,1],[1,1]]
test=[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
test1=[[1,0 ,1, 1, 0],[1 ,1, 0, 0, 1],[0, 1, 1, 1, 0],[0, 0, 0, 0, 1],[1, 1, 1, 0, 0]]
connected(test1)




