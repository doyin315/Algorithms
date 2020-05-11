from collections import deque
import copy

def highlands(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]>arr[r][c]:
            return True
        return False
    return True

def co_ordinate(arr,j,k):
    if(highlands(arr,j,k,j+1,k) and
       highlands(arr,j,k,j-1,k) and 
       highlands(arr,j,k,j,k+1) and 
       highlands(arr,j,k,j,k-1) and 
       highlands(arr,j,k,j+1,k+1) and 
       highlands(arr,j,k,j+1,k-1) and 
       highlands(arr,j,k,j-1,k+1) and 
       highlands(arr,j,k,j-1,k-1)):
        return 1
    return 0
    
def getter(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]>arr[r][c]:
            return [r,c]
        return 0
    return 0

def floodrisk(arr,p):
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
            
arr=[[1,5,3,3,9],
     [1,5,2,7,2],
     [4,5,1,7,2],
     [3,5,3,7,6],
     [4,3,6,7,3]]

arr1=[[1,1,1,1,1],
      [1,2,2,2,1],
      [1,2,3,2,1],
      [1,2,2,2,1],
      [1,1,1,1,1],
      [1,1,1,1,3]]
      
p1=[]
temp=copy.deepcopy(arr)
for j in range(len(arr)):
    l=[]
    for k in range(len(arr[0])):
        temp[j][k]=0
        if (co_ordinate(arr,j,k))==1:
            p1.append([j,k]) 
sequence=floodrisk(arr,p1)
for i in sequence:
    for j in i:
        temp[j[0]][j[1]]+=1

