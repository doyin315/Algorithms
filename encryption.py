from math import sqrt,ceil
def encryption(s):
    a=''
    root=sqrt(len(s.replace(" ","")))
    if root ==int(root):
        col=root
    else:      
        col= ceil(root)
    columns=[]
    for i in range(len(s)):
        a+=s[i]
        if len(a)==col:
            columns.append(a)
            a=''
    remainders=len(s)%col
    if remainders!=0:
        columns.append(s[int(len(s)-remainders):])

    def recursive_concat(arr,j,k):
        if j<len(arr) and k<len(arr[j]):
            return arr[j][k]+recursive_concat(arr,j+1,k)
        return ' '

    sentence=''
    for i in range(len(columns[0])):
        sentence+=recursive_concat(columns,0,i)
    return sentence



s='chillout'
encryption(s)


            
            

