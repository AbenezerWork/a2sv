class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        for i in nums:
            if i != prev+1:
                return prev+1
            prev = i
        return len(nums)