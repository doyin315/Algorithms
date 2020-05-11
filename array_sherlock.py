def rec(t):
    while len(t)>2:
        mid =len(t)//2
        left=sum(t[:2])
        right=sum(t[2:])

        if right>left:
            t=right
        else:
            t=left
    print(r)
t=[1,1,4,1,1]
s=sum(t)    
rec(t)
    


