from collections import deque
import copy
from palantir_test_2 import arr,arr1,floodrisk,getter,co_ordinate,p1

def plateaus(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]>=arr[r][c]:
            return True
        return False
    return True

def equality(arr,j,k,r,c):
    if (r>=0 and r<len(arr) and c>=0 and c<len(arr[0])):
        if arr[j][k]==arr[r][c]:
            return [r,c]
        return 0
    return 0

def plateauPoints(arr,j,k):
    if (j>=0 and j<len(arr) and k>=0 and k<len(arr[0])):
        if(plateaus(arr,j,k,j+1,k) and
        plateaus(arr,j,k,j-1,k) and 
        plateaus(arr,j,k,j,k+1) and 
        plateaus(arr,j,k,j,k-1) and 
        plateaus(arr,j,k,j+1,k+1) and 
        plateaus(arr,j,k,j+1,k-1) and 
        plateaus(arr,j,k,j-1,k+1) and 
        plateaus(arr,j,k,j-1,k-1)):
            return True
    return False

def checkIfPleateau(arr,p):
    q=deque()
    result=[]
    for i in range(len(p)):
        visited=[]
        temp=[]
        q.append(p[i])
        while len(q)!=0:
            m=0
            l=q.pop()
            x=l[0]
            y=l[1]
            if [x,y] not in visited:
                if equality(arr,x,y,x+1,y)!=0:
                    if plateauPoints(arr,x+1,y):
                        q.append([x+1,y])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x-1,y)!=0:
                    if plateauPoints(arr,x-1,y):   
                        q.append([x-1,y])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x,y+1)!=0:
                    if plateauPoints(arr,x,y+1):
                        q.append([x,y+1])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x,y-1)!=0:
                    if plateauPoints(arr,x,y-1):
                        q.append([x,y-1])
                        
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x+1,y+1)!=0:
                    if plateauPoints(arr,x+1,y+1):
                        q.append([x+1,y+1])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x+1,y-1)!=0:
                    if plateauPoints(arr,x+1,y-1):
                        q.append([x+1,y-1])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x-1,y+1)!=0:
                    if plateauPoints(arr,x-1,y+1):
                        q.append([x-1,y+1])
                    else:
                        visited=[]
                        break
                if equality(arr,x,y,x-1,y-1)!=0:
                    if plateauPoints(arr,x-1,y-1):
                        q.append([x-1,y-1])
                    else:
                        visited=[]
                        break        
                visited.append([x,y])
        t=sorted(visited)
        if t!=[] and t not in result:
            result.append(t)
    return result



p=set()
s=set()
temp=copy.deepcopy(arr)
for j in range(len(arr)):
    l=[]
    for k in range(len(arr[0])):
        if (co_ordinate(arr,j,k))==1:
            s.add((j,k))
        if plateauPoints(arr,j,k)==1:
            p.add((j,k))
        temp[j][k]=0
t=list(p-s)
result=checkIfPleateau(arr,t)
for i in result:
    for j in i:
        temp[j[0]][j[1]]=1

print(temp)
          

