seen=dict()
from collections import deque
q=deque()
def connected(arr):
    l=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==1 and not seen.get((i,j),False):
                l.append(dfs(arr,i,j,1,seen))

    return max(l)

def dfs(arr,x,y,counter,seen):
    q=deque()
    q.append((x,y))
    while q:
        l=q.popleft()
        x=l[0]
        y=l[1]
        for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
            if 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False) and arr[x1][y1]==1:
                q.append((x1,y1))
                seen[(x1,y1)]=True
                counter+=1
        seen[(x,y)]=True
    return counter

arr1=[[1,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,0,0]]
arr2=[[1,1],[1,1]]
test=[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
test1=[[1,0 ,1, 1, 0],[1 ,1, 0, 0, 1],[0, 1, 1, 1, 0],[0, 0, 0, 0, 1],[1, 1, 1, 0, 0]]
connected(test1)





# arr1=[[1,1,0,0],
#     [0,1,1,0],
#     [0,0,1,0],
#     [1,0,0,0]]

# arr2=[[1,1],[1,1]]
# test=[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
# test1=[[1,0 ,1, 1, 0],[1 ,1, 0, 0, 1],[0, 1, 1, 1, 0],[0, 0, 0, 0, 1],[1, 1, 1, 0, 0]]
# def connected(arr):
#     l=[]
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             seen=dict()
#             if arr[i][j]==1:
#                 seen[(i,j)]=True
#                 l.append(dfs(arr,i,j,1,seen))

                
#     print(l)
#     print(max(l))

# def dfs(arr,x,y,counter,seen):
#     print(counter,(x,y))
#     for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
#         if 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False):
#             seen[(x1,y1)]=True
#             if arr[x1][y1]==1:
#                 return dfs(arr,x1,y1,counter+1,seen)

#     seen[(x,y)]=False
#     return counter


# arr2=[[1,1],[1,0]]
# test=[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]

# def connected(arr):
#     l=[]
#     seen=dict()
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j]==1 and not seen.get((i,j), False):
#                 seen[(i,j)]=True
#                 l.append(dfs(arr,i,j,1))
                
#     print(l)
#     print(max(l))

# def dfs(arr,x,y,counter):
#     print(x,y)
#     for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]:
#         if 0<=x1<len(arr) and 0<=y1<len(arr[0]) and not seen.get((x1,y1),False):
#             seen[(x1,y1)]=True
#             if arr[x1][y1]==1:
#                 return dfs(arr,x1,y1,counter+1)
    
#     return counter




# connected(test)
