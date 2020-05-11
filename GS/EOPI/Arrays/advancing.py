l=[0,4,1]
furthest, last = 0, len(l) - 1
i=0
while i <= furthest and furthest < last:
    print(furthest,l[i]+1)
    furthest = max(furthest, l[i] + i)
    i+=1
print(furthest >= last)