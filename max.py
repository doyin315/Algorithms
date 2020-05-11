r=[1,2,3,4,-1,-10,3,2,14]
maxi=current=r[0]

for i in r[1:]:
    current=max(current+i,i)
    maxi=max(current,maxi)
print(maxi)