def mul(num1,num2):
    result=[0]* (len(num1)+len(num2))

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i+j+1]+=num2[i]*num1[j]
            result[i+j]+=result[i+j+1]//10
            result[i+j+1]=result[i+j+1]%10
    for i in range(len(result)):
        if result[i]!=0:
            result=result[i:]
            break
    print(result)


n=[1,2,1]
m=[1,1]
mul(n,m)