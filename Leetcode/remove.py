x1=0
v1=2
x2=5
v2=3
import math
def find(x1,v1,x2,v2):
    if (x1) < x2 and v1<v2 or x1<x2 and v2==v1 or x2>x1 and v2==v1:
        return False
    elif x1>x2 and v1>v2:
        return False
    limit=100
    while limit>0:
        x1+=v1
        x2+=v2
        limit-=1
        if x1==x2:
            return True
    return False
print(find(0,4,8,2))


print((x1 - x2) % (v2 - v1))
                     
        

