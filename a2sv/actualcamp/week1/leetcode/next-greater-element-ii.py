class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        m = {}
        for _ in range(2):
            for i in range(len(nums)):
                while stk and nums[i]>nums[stk[-1]]:
                    m[stk.pop()] = nums[i]
                stk.append(i)
        for i in range((len(nums))):
            if i in m:
                nums[i] = m[i]
            else:
                nums[i] = -1
        return nums

