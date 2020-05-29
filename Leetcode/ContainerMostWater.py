l=[1,8,6,2,5,4,8,3,7]
from math import pow
res=[]
maxFar=0
i=0
j=len(l)-1
while i<j:
    base=j-i
    height=min(l[i],l[j])
    maxFar=max(height*base,maxFar)
    print(maxFar)
    if i<j:
        i+=1
    else:
        j-=1




# l=[1,8,6,2,5,4,8,3,7]
# from math import pow
# res=[]
# maxFar=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         maxFar=max(((j-i)*(min(l[i],l[j]))),maxFar)
#         print(maxFar)
# print(maxFar)
