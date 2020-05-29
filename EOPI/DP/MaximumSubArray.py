import itertools
l=[1,2,-3,-5,-7,-2,-3,4,-5,-8,2,4,6,7]
print(sum(l))
maxfar,minfar=0,0
for i in itertools.accumulate(l):
    minfar=min(minfar,i)
    maxfar=max(maxfar,i-minfar)

print(maxfar)