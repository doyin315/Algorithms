from collections import defaultdict

d=defaultdict(int)
d[1]=2
d[0]=1

print(sorted(d.items(), key=lambda x:x[1], reverse=True)[0][0])