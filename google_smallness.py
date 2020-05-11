import string
def smallness(a,b):
    a+=' '
    b+=' '
    l=[]  
    result=[]
    alpha=string.ascii_lowercase
    for i in range(len(b)):
        temp=0
        b_count=0
        if b[i]!=' ' and i!=len(b)-1:
            l.append(alpha.index(b[i]))
        else:
            b_count+=b[len(b)-len(b[i:])-len(l):i+1].count(alpha[min(l)])
            l.clear()
            for j in range(len(a)):
                a_count=0
                if a[j]!=' ':
                    l.append(alpha.index(a[j]))
                else:
                    a_count+=a[len(a)-len(a[j:])-len(l):j+1].count(alpha[min(l)])
                    if a_count<b_count:
                        temp+=1
                    l.clear()   
        if temp!=0:
            result.append(temp)
    print(result) 

            
A='abcd aabc bad abaaabaaa'
B='aaa aa aba'      
smallness(A,B)
                    
                 
