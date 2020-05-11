l=[1,4,3,2,6,0,2,5,3,2]

def arrange(result,index):
    num=result[index]
    small=0
    large=len(result)-1
    for i in range(len(result)):
        if result[i]<num:
            result[small],result[i]=result[i],result[small]
            small+=1

    for i in reversed(range(len(result))):
        if result[i]<num:
            break
        if result[i]>num:
            result[large],result[i]=result[i],result[large]
            large-=1
    print(result)



# def Arrange(arr, index):
#   end = len(arr) - 1
#   arr[index], arr[end] = arr[end], arr[index]
#   leader, follower = 0, 0
#   while leader < end:
#     if arr[leader] <= arr[end]:
#       arr[follower], arr[leader] = arr[leader], arr[follower]
#       follower += 1
#     leader += 1
#   arr[follower], arr[end] = arr[end], arr[follower]
#   for i in range(follower):
#     if arr[i] == arr[follower]:
#       arr[follower-1], arr[i] = arr[i], arr[follower - 1]
#   print(arr)
#   print(arr)


l=[1,4,3,2,6,0,2,5,2]
ind=3
arrange(l,3)
