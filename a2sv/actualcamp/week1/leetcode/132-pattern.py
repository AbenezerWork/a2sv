class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        mx = -float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<mx:
                return True
            if stk and stk[-1]<nums[i]:
                while stk and stk[-1]<nums[i]:
                    mx = max(mx,stk.pop())

            stk.append(nums[i])
        return False
            