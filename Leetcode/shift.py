from collections import defaultdict
def shifter(s,shift):
    d=defaultdict(int)
    for i in shift:
        d[i[0]]+=i[1]
    
    arr=[i for i in s]
    for i in d:
        if i==0:
            for _ in range(d[i]):
                temp=arr[0]
                for j in range(len(arr)-1):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    print(arr)   
        else:
            for _ in range(d[i]):
                for j in reversed(range(1,len(arr))):
                    print(j)
                    arr[j],arr[j-1]=arr[j-1],arr[j]   

            


s="abc"
shift = [[0,1]]
shifter(s,shift)

# l=[i for i in s]
# temp=l[0]

# for i in range(len(l)-1):
#     l[i],l[i+1]=l[i+1],l[i]
# l[-1]=temp

# print(l)
