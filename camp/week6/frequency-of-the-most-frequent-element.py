class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sum = 0
        j =0
        mx = 0
        nums.sort()
        for i in range(len(nums)):
            sum+=nums[i]
            op = (i-j+1)*nums[i]-sum
            while j<=i and  op >k:
                op-=nums[i]-nums[j]
                sum-=nums[j]
                j+=1
            mx = max(i-j+1,mx)
        return mx
