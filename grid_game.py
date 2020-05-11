def co_ordinate(arr,j,k):
    n=0
    if j==0 and k==0: #top left
        n+=arr[0][1]+arr[1][0]+arr[1][1]
    elif j==0 and k==len(arr[0])-1: #top right
        n+=arr[0][len(arr[0])-2]+arr[1][len(arr[0])-1]+arr[1][len(arr[0])-2]
    elif j==len(arr)-1 and k==0: #bottom left
            n+=arr[len(arr)-2][0]+arr[len(arr)-1][1]+arr[len(arr)-2][1]
    elif j==len(arr)-1 and k==len(arr[0])-1: #bottom right
            n+=arr[len(arr)-1][len(arr[0])-2]+arr[len(arr)-2][len(arr[0])-2]+arr[len(arr)-2][len(arr[0])-1]
    else:
        if k==0: #first column
            n+=arr[j-1][k]+arr[j+1][k]+arr[j][k+1]+arr[j-1][k-1]+arr[j+1][k+1]
        elif k==len(arr[0])-1: #last column
            n+=arr[j-1][k]+arr[j+1][k]+arr[j][k-1]+arr[j-1][k-1]+arr[j+1][k-1]
        elif j==0: #first row
            n+=arr[j][k-1]+arr[j][k+1]+arr[j+1][k]+arr[j-1][k-1]+arr[j+1][k+1]
        elif j==len(arr)-1: #last row
            n+=arr[j][k-1]+arr[j-1][k-1]+arr[j-1][k]+arr[j-1][k+1]+arr[j][k+1]
        else:
            n+=arr[j-1][k]+arr[j+1][k]+arr[j][k+1]+arr[j][k-1]+arr[j-1][k-1]+arr[j-1][k+1]+arr[j+1][k-1]+arr[j+1][k+1]
    return n

turns=2
arr=[[1,0],[0,1],[0,0]]

p=[]
rules=['dead','alive','dead','dead','dead','dead','dead','dead','dead']

for j in range(len(arr)):
    l=[]
    for k in range(len(arr[0])):
        l.append(co_ordinate(arr,j,k))
    p.append(l)
print(p)

    
            








