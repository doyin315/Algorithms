def reverse(s,start,end):
    if start<end-1:
        s[start],s[end-1]=s[end-1],s[start]
        reverse(s,start+1,end-1)
s=[1,2,3,4,5]
reverse(s,0,len(s))