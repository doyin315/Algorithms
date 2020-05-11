d={'{':'}','[':']','(':')'}

s='([]))'
stack=[]
for i in s:
    if i in d:
        stack.append(i)
    else:
        if not stack or d[stack.pop()]!=i:
            print("false")
    print("true")
