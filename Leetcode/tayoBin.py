
def binary_search(arr,value,search_type):
    '''
    
    [1,1,1]
    l = 2
    r = 2
    
    mid = 2
    '''
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = l + ((r-l) // 2)
        if arr[mid] < value:
            l = mid+1
        elif arr[mid] > value:
            r = mid-1
        else:
            # arr[mid] == value
            if search_type == START_SEARCH_TYPE:
                if mid == 0 or arr[mid-1] != value:
                    return mid
                else:
                    r = mid-1
            else:
                if mid == len(arr)-1 or arr[mid+1] != value:
                    return mid
                else:
                    l = mid+1
    return -1
                
                
            
        
'''
[1,1,2,2,3]
v = 2
v = 3


[1,1,1,1,1,1]
v = 1
'''
    

def find_find_and_last_occurrence(arr,value):
    if len(arr) == 0:
        return [-1,-1]
    
    result = [binary_search(arr,value,START_SEARCH_TYPE),binary_search(arr,value,END_SEARCH_TYPE)]
    return result
