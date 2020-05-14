def pow(x,n):
    temp=x
    while n>1:
        n-=1
        x*=temp

        
    print(x)

pow(2,31)