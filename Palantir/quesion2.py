# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]


# word = 'ABE'




from collections import deque
import copy
from quesion1 import arr,arr1,co_ordinate

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

def main():   
    p=[]
    temp=copy.deepcopy(arr1)
    for j in range(len(arr1)):
        l=[]
        for k in range(len(arr1[0])):
            temp[j][k]=0
            if (co_ordinate(arr1,j,k))==1:
                p.append([j,k]) 
    sequence=floodrisk(arr1,p)
    for i in sequence:
        for j in i:
            temp[j[0]][j[1]]+=1
    return temp

