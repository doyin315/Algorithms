def binary_search(arr,ele):
    first=0
    last=len(arr)-1

    found=False

    while first<=last and not found:
        mid=(first+last)//2

        if ele==mid:
            found=True
        elif ele<mid:
            last=mid-1
        else:
            first=mid+1
    return found

print(binary_search([1,2,3,4,6],9))