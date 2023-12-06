class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        mxPer = 0
        nums.sort()
        for i in range(len(nums[:-2])):
            if nums[i]+nums[i+1] > nums[i+2] and nums[i+1] + nums[i+2] >nums[i] and nums[i] + nums[i+2] > nums[i+1]:
                mxPer = max(nums[i]+nums[i+1]+nums[i+2], mxPer)
        return mxPer