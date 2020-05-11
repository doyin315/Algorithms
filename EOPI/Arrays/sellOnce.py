l=[310,315,275,295,260,270,290,230,255,250]
min_so_far=l[0]
current=0
profit=0
for i in range(1,len(l)):
    min_so_far=min(min_so_far,l[i])
    profit=max(profit,l[i]-min_so_far)

print(profit)
    
        