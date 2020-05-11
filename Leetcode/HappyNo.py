num=19
from math import pow

def happy(n):
    if n<10:
        if n==1 or n==7:
            return True
        else:
            return False

    n=sum([int(pow(int(i),2)) for i in str(n)])
    return happy(n)


print(happy(26))



