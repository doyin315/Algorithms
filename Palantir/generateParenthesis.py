def generate(n,open=0,close=0,s=[],res=[]):
    if open<n:
        s.append('(')
        generate(n,open+1,close,s,res)
        s.pop()
    
    if close<open:
   s.append('(')
        generate(n,open+1,close,s,res)
        s.pop()
