def missing(arr):
    d={}
    start=1
    found=False
    for i in arr:
        d[i]=True

    while True:
        if not d.get(start, False):
            break
        start+=1

    print(start)

l=[7,8,9,11,12]
missing(l)

    
