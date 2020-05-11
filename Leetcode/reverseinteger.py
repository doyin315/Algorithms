import math
def reverse( x: int) -> int:
    t=[i for i in str(x)]
    if x<0:
        res=0-(int(('').join(t[-1:0:-1])))
    else:
        res=int(('').join(t[-1::-1]))
    if res> (math.pow(2,31))-1:
        return 0
    elif res< (0-(math.pow(2,31))-1):
        return 0
    elif res<0:
        return 0-int(('').join(t[-1:0:-1]))
        
    return res

print(reverse(1534236469))
