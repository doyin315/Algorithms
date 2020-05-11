m=[-2,0,1,1,2]
n=[3,0,-2,-1,1,2]
def solution(arr):
    d=dict()
    for i in range(len(arr)-2):
        seen=set()
        target=arr[i]
        for j in range(i+1,len(arr)):     
            sub=0-(target+arr[j])
            if sub not in seen:
                seen.add(arr[j])
            else:
                pack=tuple(sorted((arr[j],sub,target)))
                if not d.get(pack, False):
                    d[tuple(pack)]=True

    return [list(i) for i in d.keys()]

print(solution(n))
