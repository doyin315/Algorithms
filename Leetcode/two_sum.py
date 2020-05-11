
dic={}
nums=[2,7,11,5]
target=9
d=set()
for i in range(len(nums)):
    dic[nums[i]]=i
    p=target-nums[i]
    if p in d:       
        ans=[dic[min(nums[i],p)],dic[max(nums[i],p)]]
    else:
        d.add(nums[i])
print(ans)

"""from collections import defaultdict 
class Solution:
    dic=defaultdict(int)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=set()
        for i in range(len(nums)):
            dic[nums[i]]=i
            p=target-nums[i]
            if p in d:
                ans=[dic[min(nums[i],p)],dic[max(nums[i],p)]]
            else:
                d.add(nums[i])
        return ans
                     
        """