import operator
def chain(arr):
    cur,ans= float('-inf'),0
    for i,j in sorted(arr,key=lambda x: x[1]):
        if cur<i:
            cur=j
            ans+=1
        print(ans)
    print(ans)
    





l =[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]

print(sorted(l,key=lambda x: x[1]))

print(float('-inf'))
chain(l)

def chainer(pairs):
    count=1
    pairs=sorted(pairs, key=lambda x :x[1])
    current=pairs[0][1]
    for i in range(1,len(pairs)):
        if pairs[i][0]>current:
            count+=1
            current=pairs[i][1]
    print(count)
    return count

chainer(l)