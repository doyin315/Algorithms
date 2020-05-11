from collections import defaultdict
l=[[80,96,81,77],[78,71,93,75,],
[71,98,70,95],[80,96,89,77]]
r=3
d=defaultdict(int)
for i in range(len(l)):
    d[i]=sum(l[i])
print(d)
print(sorted(d.items(), key = lambda x : x[1], reverse=True))
