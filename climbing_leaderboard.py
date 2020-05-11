scores=[100,100,50,40,40,20,10]
alice=[5,25,50,120]
l=[]
scores=list(dict.fromkeys(scores))
d=(len(scores)-1)
for i in alice:
    while True:
        if i<scores[-1]:
            l.append(len(scores)+1)
            break
        elif i>=scores[0]:
            l.append(1)
            break
        elif i>=scores[d] and i<scores[d-1]:
            l.append(d+1)
            break
            d-=1
        else:
            d-=1
print(l)
        
