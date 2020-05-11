from collections import defaultdict
def maximumOccurringCharacter(text):
    d=defaultdict(int)
    for i in text:
        d[i]+=1
    sorted_d=sorted(d.items(), key=lambda x:x[1], reverse=True)
    print(sorted_d)
    return sorted_d[0][0]

text="hello world"

print(maximumOccurringCharacter(text))