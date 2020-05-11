
def bisum(l):
    t=l
    c=[]
    for i in enumerate(l):
        c.append(i)
    print(c)
    while len(t)>2:
        mid=len(t)//2
        left=t[:mid]
        right=t[mid:]
        if right>left:
            t=right
        else:
            t=left


l=[1,2,6,3,3,13]
t=l
bisum(l)