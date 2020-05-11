n=2
def generate(open,close,s=[]):
    if close==n:
        print(s)

    else:
        if open>close:
            s.append(')')
            generate(open,close+1,s)
            s.pop()

        if open<n:
            s.append('(')
            generate(open+1,close,s)
            s.pop()

generate(0,0,[])