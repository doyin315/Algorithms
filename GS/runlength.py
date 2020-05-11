def runlength(a):
    temp=a[0]
    count=0
    ans=''
    for i in range(len(a)):
        if i!=len(a)-1:
            if a[i] == temp:
                count+=1
            else:
                ans+=str(count)+temp
                temp=a[i]
                count=1
        else:
            if a[i]==temp:
                count+=1
                ans+=str(count)+temp
            else:
                ans+=str(count) + temp
                ans+='1'+ a [i]
    return ans


print(runlength('rrrryye'))