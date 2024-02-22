class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stk = []
        ans = [0]*len(nums)
        for i in range(len(nums)):
            while stk and nums[stk[-1]]<nums[i]:
                ans[stk[-1]] = i-stk[-1]
                stk.pop()
            stk.append(i)
        return ans