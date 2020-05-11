def add(n):
    t=str(abs(n))
    c=0
    l=[c for c in t]
    print(l)
    if n>0:
        for i in range(len(l)):
            n=abs(n)
            if 5>int(l[i]):
                l.insert(i,'5')
                return int(''.join(l))
                break
        l.append('5')
        return int(''.join(l))
    else:
        for i in range(len(l)):
            if 5<int(l[i]):
                l.insert(i,'5')
                return (0-int(''.join(l)))
                break
        l.insert(0,5)
        return (0-int(''.join(l)))

          

print(add(646))