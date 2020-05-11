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
            
arr=[[1,2,1,3,4],
     [1,5,2,2,2],
     [4,5,1,9,2],
     [3,5,3,7,6],
     [4,3,1,7,3]]

arr1=[[1,1,1,1,1],
      [1,2,2,2,1],
      [1,2,3,2,1],
      [1,2,2,2,1],
      [1,1,1,1,1],
      [1,1,1,1,3]]

def main():  
    p1=[]
    temp=copy.deepcopy(arr)
    for j in range(len(arr)):
        l=[]
        for k in range(len(arr[0])):
            temp[j][k]=0
            if (co_ordinate(arr,j,k))==1:
                p1.append([j,k]) 
    for i in p1:
        temp[i[0]][i[1]]=1

    return temp


print(main())