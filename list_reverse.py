def reverse(s,start, stop):
    if start<stop-1:
        s[start], s[stop-1] = s[stop-1],s[start]
        reverse(s,start+1,stop-1)
    else:
        print(s)
t=[4,3,6,2,8,9,5]

reverse(t,0,len(t))