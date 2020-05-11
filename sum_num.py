d=[1,2,4,3,3,2,5]
k=4
def find(d,k):
    r=set()
    for i in d:
        t=k-i
        if t in d:
            r.add((max(i,t),min(i,t)))
        else:
            continue
    print(r)
find(d,k)
