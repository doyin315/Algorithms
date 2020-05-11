def reverse(s):
    a=''
    final=''
    for i in range(len(s)-1,-1,-1):
        a+=s[i]
    word_list=a.split(' ')
    for j in range(len(word_list)-1,0,-1):
        final+=word_list[j]+ ' '
    final+=word_list[0]

    return final

print(reverse('hello world'))
    
from collections import defaultdict
def unique(t):
    d=defaultdict(int)
    for i in t:
        d[i]+=1

    for j in d:
        if d[j]==1:
            return j


print(unique('racecars'))

def repeat(t):
    d=defaultdict(int)
    for i in t:
        d[i]+=1

    for j in d:
        if d[j]>1:
            return 'weak'
    return 'strong'

