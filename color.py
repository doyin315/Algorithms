a='colour'
l=[]
for i in range(len(a)):
    for j in range(len(a)+1):
        if a[i:j]!='':
            l.append(a[i:j])
print(len(l))
d=[]
y=[]
for i in a:
    d.append(i)
for i in range(len(a)):
    for j in range(len(a)+1):
        if (''.join(d[i:j]))!='':
            y.append((''.join(d[i:j])))

print(y)