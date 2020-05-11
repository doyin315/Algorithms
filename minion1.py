def minion_game(string):
    vowel = ['A','E','I','O','U']
    st=0
    k=0
    for i  in range(len(string)):
        if string[i] in vowel:
            k+=len(string[i:])
        else:
            st+=len(string[i:])
    if k>st:
        print("Kevin {}".format(k))
    elif st>k:
        print("Stuart {}".format(st))
    else:
        print("Draw")

minion_game('BANANA')