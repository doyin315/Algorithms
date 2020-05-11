"""t=3
for _ in range(t):
    l=int(input("Enter Number: "))
    result=0
    for j in range(1,l+1):
        count=0
        for i in range(1,j+1):
            if j%i==0:
                count+=1         
        if count==3:
            print(j,i)
            result+=1
    print(result)"""


t=3
for _ in range(t):
    l=int(input("Enter Number: "))
    result=0
    for j in range(1,l):
        count=0
        for i in range(2,j):
            if j%i==0:
                count+=1
                if count>1:
                    continue
        if count==3:
            print(j,i)
            result+=1
    print(result)

