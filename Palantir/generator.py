def gen(n):
    a=0
    for i in range(n):
        yield a
        a+=2

t=gen(10)

import random
def rand(low,high,n):

    for i in range(n):
        yield(random.randint(low,high))


for i in rand(1,10,12):
    print(i)