l= [-1, 0, 1, 2, -1, -4]
t=[3,0,-2,-1,1,2]
def solution(arr):
    arr=sorted(arr)
    d={}
    for i in range(len(arr)-1):

        j,k=i+1, len(arr)-1
        a=arr[i]
        while j<k:
            b=arr[j]
            c=arr[k]
            if a+b+c==0:
                print(a,b,c)
                d[tuple(sorted((a,b,c)))]=True
                j+=1
                k-=1
            elif a+b+c<0:
                j+=1
            else:
                k-=1
    print([list(i) for i in d.keys()])

solution(t)























