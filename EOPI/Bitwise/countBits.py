def count_bits (x) :
    num_bits = 0
    while x:
        print(x)
        num_bits+=x&1
        x>>=1
    return num_bits

b=5

print(count_bits(b))