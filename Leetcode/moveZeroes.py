nums= [0,1,0,3,12]

start=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[start],nums[i]=nums[i],nums[start]
        start+=1
print(nums)
    