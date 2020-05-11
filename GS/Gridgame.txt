from collections import defaultdict
d=defaultdict(int)
arr=[[0,1,1,0],[1,1,0,0]]

def getter(arr,j,k):
    if(j>=0 and j<len(arr) and k>=0 and k<len(arr[0])):
        return arr[j][k]
    else:
        return 0

def nsum(arr,j,k):
    return getter(arr,j,k+1)+getter(arr,j,k-1)+getter(arr,j+1,k+1)+getter(arr,j+1,k-1)+getter(arr,j-1,k+1)+getter(arr,j-1,k-1)+getter(arr,j+1,k)+getter(arr,j-1,k)

def gridgame():
    rules=['dead', 'dead','dead', 'alive','dead','alive', 'dead','dead', 'dead']
    for i in range(len(rules)):
        d[i]=rules[i]
    print(d)
    l=[]
    turns=2
    for _ in turns:
        for j in range(len(arr)):
            p=[]
            for k in range(len(arr[0])):
                print(nsum(arr,j,k))
                if d[nsum(arr,j,k)]=='alive':
                    p.append(1)
                else:
                    p.append(0)
            l.append(p)
        print(l)

gridgame()