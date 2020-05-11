s="ab##"
t="c#d#"

i=len(s)-1
j=len(t)-1
shash=0
thash=0
news=""
newt=""
while 0<=i<len(s):
    if s[i]=="#":
        i-=1
        shash+=1
 
    elif shash==0:
        news+=s[i]
        i-=1

    elif shash>0:
        shash-=1
        i-=1

while 0<=j<len(t):
    if t[j]=="#":
        thash+=1
        j-=1
    elif thash==0:
        newt+=t[j] 
        j-=1
    elif thash>0:
        thash-=1
        j-=1

print(news,newt)