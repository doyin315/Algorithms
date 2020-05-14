def plus(digits):
    rem=1
    for i in range(len(digits)-1,-1,-1):
        digits[i]+=rem
        rem=digits[i]//10
        digits[i]%=10
    if rem!=0:
        digits.append(rem)
        return list(reversed(digits))
    return digits

l=[9,9,9]
print(plus(l))
        
        