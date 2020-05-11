mapping=('','','abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz')
def phone_mnemonic(phone_number) :
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            print(mnemonics,partial_mnemonic,2)
            mnemonics.append(('').join(partial_mnemonic))
        else:
            for c in mapping[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                print(mnemonics,partial_mnemonic,1)
                phone_mnemonic_helper(digit + 1)

    mnemonics, partial_mnemonic = [] , [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

print(phone_mnemonic([2,3]))