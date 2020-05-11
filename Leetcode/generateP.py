def generate(n,open=0,closed=0,s=[],store=[]):
    if closed==n:
        store.append(''.join(s))
        print(store)

    if open>closed:
        s.append(')')
        generate(n,open,closed+1,s,store)
        s.pop()

    if open<n:
        s.append('(')
        generate(n,open+1,closed,s,store)
        s.pop()



generate(2)
