dividend=2147
divisor=10
if dividend<0 or divisor<0:
    neg=True
count=0

while dividend>=divisor:
    dividend-=divisor
    count+=1
    print(dividend,count)

print(count)

import math

print(int(math.pow(2,31)))