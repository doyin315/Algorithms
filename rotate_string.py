from collections import defaultdict
def rotate(a,s_r,s_amount):
    d=defaultdict(int)
    for s,r in zip(s_r,s_amount):
        d[s]+=r
    for i in list(d.keys()):
        if i == 0:
            for j in range(d[i]):
                temp=a[1:]+a[0]
                a=temp
        elif i == 1:
            for j in range(d[i]):
               temp=a[-1]+a[:len(a)]
               a=temp
    return a


print(rotate('isrightbenny',[0,0],[3,4]))

