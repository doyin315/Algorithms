s='a#b'
t= 'b'
scount=s.count('#')
tcount=t.count('#')
if len(s)-(2*scount)!=len(t)-(2*tcount):
    print('false',scount,tcount)
i=0
j=0

while i<len(s)-1 and j<len(t)-1:
    if s[i+1]!='#' and t[j+1]!='#':
        if s[i]==t[j]:
            i+=1
            j+=1
        else:
            print("false")
    elif s[i+1] =='#' and t[j+1]=='#':
        i+=2
        j+=2
    elif s[i+1] =='#' and t[j+1]!='#':
        i+=2
    elif t[j+1]=='#':
        j+=2

print(i,j)

while i<len(s)-1:
    if s[i+1]=='#':
        i+=2
        if s[i]==t[j]:
            print('True')
        else:
            print('false')
        i+=1
        j+=1


while j<len(t)-1:
    if t[i+1]=='#':
        j+=2
        if s[i]==t[j]:
            print('True')
        else:
            print('false')
        i+=1
        j+=1
            
            
            
            