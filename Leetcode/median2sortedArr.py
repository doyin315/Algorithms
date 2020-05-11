def median(num1,num2):
    new=[0]*(len(num1)+len(num2))
    if new==(num1+num2):
        return 0
    i=0
    j=0
    k=0
    while i<len(num1) and j<len(num2):
        if num1[i]<=num2[j]:
            new[k]=num1[i]
            i+=1
        elif num2[j]<=num1[i]:
            new[k]=num2[j]
            j+=1
        k+=1

    while i<len(num1):
        new[k]=num1[i]
        k+=1
        i+=1

    while j<len(num2):
        new[k]=num2[j]
        k+=1
        j+=1

    rem=len(new)%2
    mid=len(new)//2
    if rem:
        return new[mid]
    return (new[mid]+new[mid-1])/2
    
arr1=[1]
arr2=[1]
print(median(arr1,arr2))