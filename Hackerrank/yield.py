def ret():
    for i in range(4):
        yield i

print([i for i in ret()])