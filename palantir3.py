from collections import deque
def co_ordinate(arr,j,k):
    if(plateau(arr,j,k,j+1,k) and
       plateau(arr,j,k,j-1,k) and 
       plateau(arr,j,k,j,k+1) and 
       plateau(arr,j,k,j,k-1) and 
       plateau(arr,j,k,j+1,k+1) and 
       plateau(arr,j,k,j+1,k-1) and 
       plateau(arr,j,k,j-1,k+1) and 
       plateau(arr,j,k,j-1,k-1)):
        return 1
    return 0

def getter(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]>arr[r][c]:
            return [r,c]
        return 0
    return 0

def plateau(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]>=arr[r][c]:
            return True
        return False
    return True
def identity(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]==arr[r][c]:
            return True
        return False
    return True

def connected(arr,p):
    visited=[]
    q=deque()
    result=[]
    for i in range(len(p)):
        q.append(p[i])
        while len(q)!=0:
            l=q.pop()
            x=l[0]
            y=l[1]
            if [x,y] not in visited:
                if getter(arr,x,y,x+1,y)!=0:
                    q.append(getter(arr,x,y,x+1,y))
                if getter(arr,x,y,x-1,y)!=0:
                    q.append(getter(arr,x,y,x-1,y))
                if getter(arr,x,y,x,y+1)!=0:
                    q.append(getter(arr,x,y,x,y+1))
                if getter(arr,x,y,x,y-1)!=0:
                    q.append(getter(arr,x,y,x,y-1))
                if getter(arr,x,y,x+1,y+1)!=0:
                    q.append(getter(arr,x,y,x+1,y+1))
                if getter(arr,x,y,x+1,y-1)!=0:
                    q.append(getter(arr,x,y,x+1,y-1))
                if getter(arr,x,y,x-1,y+1)!=0:
                    q.append(getter(arr,x,y,x-1,y+1))
                if getter(arr,x,y,x-1,y-1)!=0:
                    q.append(getter(arr,x,y,x-1,y-1))
                visited.append([x,y])
        result.append(visited)
        visited=[]
    return result


arr=[[1,2,1,3,4],
     [1,5,2,2,2],
     [4,5,1,9,7],
     [3,5,3,7,6],
     [4,3,1,7,3]]

arr1=[[1,1,1,1,1],
      [1,2,2,2,1],
      [1,2,3,2,1],
      [1,2,2,2,1],
      [1,1,1,1,1],
      [1,1,1,1,3]]
      
p=[]
for j in range(len(arr)):
    l=[]
    for k in range(len(arr[0])):
        l.append(co_ordinate(arr,j,k))
    p.append(l) 
print(p)