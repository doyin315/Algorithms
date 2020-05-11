
def strangeSort(mapping, nums):
    mapDictionary = {}
    reverseMap = {}
    
    for mapper in mapping:
        mapDictionary [str(mapper)] = str(mapping.index(mapper))
        reverseMap[str(mapping.index(mapper))] = str(mapper)
    
    convertedArray = arrayConversion(nums, mapDictionary)
    print(convertedArray)
    sortedArray = mergeSort(convertedArray)
    print(sortedArray)
    reversedConverted = arrayConversion(sortedArray, reverseMap)
    
    return reversedConverted
        
def arrayConversion(string, dictionary):
        convertedArray = []
        for stringg in string:
            sub_string = ""
            for stringer in stringg:
                sub_string += dictionary[stringer]
            convertedArray.append(sub_string)
        return convertedArray
            
            
        
def mergeSort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if int(lefthalf[i]) <= int(righthalf[j]):
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
            
    return alist
    
mapping=[3,5,4,6,2,7,9,8,0,1]
nums=['990','332','32']

print(strangeSort(mapping,nums))


