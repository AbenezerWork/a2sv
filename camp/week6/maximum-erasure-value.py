class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = set()
        j = 0
        mx,sum = 0,0
        for i in range(len(nums)):
            sum+=nums[i]
            if nums[i] in dic:
                while nums[i]!=nums[j]:
                    dic.discard(nums[j])
                    sum-=nums[j]
                    j+=1
                j+=1
                sum-=nums[i]
            mx = max(mx,sum)
            dic.add(nums[i])
        return mx

            