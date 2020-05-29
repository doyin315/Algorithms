def jump(nums):
    count=0

    current=len(nums)
    clear=len(nums)-1
    while current>=0:
        print(current,'curr')
        for j in reversed(range(current)):
            if nums[j]+j>=clear:
               pos=j
               print(pos,j)
        current=pos
        clear=current
        count+=1
        if current==0:
            break
    print(count,'count')
   

l=[2,3,1,1,4]

jump(l)

