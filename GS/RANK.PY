from collections import defaultdict
d=defaultdict(int)
k=2
scores=[[79,89,15],[85,89,92],[71,96,88]]
for i in range(len(scores)):
    d[i]=sum(scores[i])
l=sorted(d.items(),key=lambda x:x[1])
print(l[k-1][0])