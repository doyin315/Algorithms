
num1=[1,1,2]
num2=[1,1]
result = [0] * (len(num1) + len(num2))
for i in reversed(range(len(num1))) :
    for j in reversed(range(len(num2))) :
        result[i + j + 1] += num1[i] * num2[j]
        result[i + j] += result[i + j + 1] // 10
        result[i+j+1]%=10

print(result)

print(next((i for i , x in enumerate(result) if x!=0), len(result))
