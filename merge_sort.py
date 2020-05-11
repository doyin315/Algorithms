def merge_sort(arr):
    if len(arr)>1:

        mid=len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0
        print(lefthalf,righthalf)
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            arr[k] =righthalf[j]
            j+=1
            k+=1
arr1=[5,1,3,2]
arr=[8,6,43,6,3,2,19]
merge_sort(arr1)
print(arr1)