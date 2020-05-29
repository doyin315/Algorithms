def position(arr,k):
    def find(arr,num,type):
        if len(arr)==0:
            return -1
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = left + ((right-left) // 2)
            if arr[mid] < num:
                left = mid+1
            elif arr[mid] > num:
                right = mid-1
            else:
                if type == 'start':
                    if mid==0 or arr[mid-1]!=num:
                        return mid
                    else:
                        right=mid-1
                else:
                    if mid==len(arr)-1 or arr[mid+1]!=num:
                        return mid
                    else:
                        left=mid+1

        return -1

    return [find(arr,k,'start'), find(arr,k ,'end')]

l=[2,3,1,1,1,5]
print(position(l,1))