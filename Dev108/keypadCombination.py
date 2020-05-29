arr=['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

def combinations(l):
    result=[]
    temp=[0]*len(l)

    def backtrack(num):
        if num == len(l):
            result.append(('').join(temp))
        else:
            for i in arr[l[num]]:
                temp[num]=i
                backtrack(num+1)

    backtrack(0)
    return result

r=[2,3]
print(combinations(r))

