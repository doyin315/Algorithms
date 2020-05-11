mapping=('','','abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz')

def letterCombinations( digits):
    res,partial=[],[0]*len(digits)
    def combine(num):
        if num==len(partial):
            res.append(('').join(partial))

        else:
            for i in mapping[int(digits[num])]:
                partial[num]=i
                combine(num+1)
    combine(0)

    print(res)


letterCombinations("")

        
    
print(len(['']))