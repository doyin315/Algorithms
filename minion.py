"""from collections import defaultdict
def minion(s):
    stuart=0
    kevin=0
    vowels=['A','E','I','O','U']
    d=defaultdict(int)
    for i in range(len(s)):
        for j in range(len(s)+1):
            if s[i:j]!='':
                d[s[i:j]]+=1
    for i in d:
        if i[0] in vowels:
            kevin+=d[i]
        else:
            stuart+=d[i]
    print(kevin,stuart)
           
s='BANANA'
minion(s)"""


def mini(s):
    st=0
    k=0
    vowels=['A','E','I','O','U']
    for i in range(len(s)):
        if s[i] in vowels:
            k+=len(s)-i
        else:
            st+=len(s)-i
    print(st,k)
s='BANANA'
mini(s)

    

        