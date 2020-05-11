mapping=('','','abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz')

def phone(nums):
    code, partialcode= [],[0]*len(nums)
    def comb(digit):
        if digit==len(partialcode):
            code.append(('').join(partialcode))
        else:
            for i in mapping[nums[digit]]:
                partialcode[digit]=i
                comb(digit+1)
    comb(0)

phone([2,3])

l=[1,2]
l.pop(0)
print(l)