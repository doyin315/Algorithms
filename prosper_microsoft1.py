def solution(s,k):
    l=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    i=l.index(s)
    if l[i]==s:
        day=i+k
        if day<len(l):
            return l[day]
        else:
            day%=7
            return l[day]

print(solution("Sun", 2))

