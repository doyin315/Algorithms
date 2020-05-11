def co_ordinate(arr,j,k):
    n=arr[j][k]
    if len(arr)==1:
        if j==0 and arr[0][1]>=arr[0][0]: return 0
        elif k==len(arr[0]-1) and arr[0][len(arr[0])-2]>=arr[0][len(arr[0]-1)]: return 0
        elif arr[j][k-1]>=n or arr[j][k+1]>=n: return 0
    if j==0 and k==0 and arr[0][1]>=n or arr[1][0]>=n or arr[1][1]>=n: return 0 #top left
    elif j==0 and k==len(arr[0])-1 and arr[0][len(arr[0])-2]>=n or arr[1][len(arr[0])-1]>=n or arr[1][len(arr[0])-2]>=n: return 0  #top right
    elif j==len(arr)-1 and k==0 and arr[len(arr)-2][0]>=n or arr[len(arr)-1][1]>=n or arr[len(arr)-2][1]>=n: return 0  #bottom left
    elif j==len(arr)-1 and k==len(arr[0])-1 and arr[len(arr)-1][len(arr[0])-2]>=n or arr[len(arr)-2][len(arr[0])-2]>=n or arr[len(arr)-2][len(arr[0])-1]>=n: return 0 #bottom right
    elif k==0 and arr[j-1][k]>=n or arr[j+1][k]>=n or arr[j][k+1]>=n or arr[j-1][k-1]>=n or arr[j+1][k+1]>=n: return 0 #first column
    elif k==len(arr[0])-1 and arr[j-1][k]>=n or arr[j+1][k]>=n or arr[j][k-1]>=n or arr[j-1][k-1]>=n or arr[j+1][k-1]>=n: return 0 #last column
    elif j==0 and arr[j][k-1]>=n or arr[j][k+1]>=n or arr[j+1][k]>=n or arr[j-1][k-1]>=n or arr[j+1][k+1]>=n: return 0 #first row
    elif j==len(arr)-1 and arr[j][k-1]>=n or arr[j-1][k-1]>=n or arr[j-1][k]>=n or arr[j-1][k+1]>=n or arr[j][k+1]>=n: return 0 #last row
    elif arr[j-1][k]>=n or arr[j+1][k]>=n or arr[j][k+1]>=n or arr[j][k-1]>=n or arr[j-1][k-1]>=n or arr[j-1][k+1]>=n or arr[j+1][k-1]>=n or arr[j+1][k+1]>=n: return 0
    return 1
arr=[[1,2,1,3,4],[1,5,2,2,2],[4,5,1,9,7],[3,5,3,7,6],[4,3,1,7,3]]
arr1=[[1,1,1,1,1],[1,2,2,2,1],[1,2,3,2,1],[1,2,2,2,1],[1,1,1,1,1],[1,1,1,1,3]]
p=[]
for j in range(len(arr)):
    l=[]
    for k in range(len(arr[0])):
        l.append(co_ordinate(arr,j,k))
    p.append(l)
print(p)

    
             








