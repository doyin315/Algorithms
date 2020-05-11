nums=[3,2,4]
target=6
for i in range(len(nums)):
    t=target-nums[i]
    if t in nums:
        print([i,nums.index(t)])
