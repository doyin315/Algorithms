def powers(n):
    l=[]
    num=1
    while num<=n:
        l.append(num)
        num*=2
    return(l)
print(powers(2))