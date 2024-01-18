class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        ans = 0
        d[0]+=1
        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        print(nums)
        for i in range(len(nums)):
            ans+=d[nums[i]-goal]
            d[nums[i]]+=1
        return ans