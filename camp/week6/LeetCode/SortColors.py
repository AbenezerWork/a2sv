class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for k in range(len(nums)):
            if nums[k] == 0:
                nums[k],nums[i] = nums[i], nums[k]
                i+=1
        for k in range(i,len(nums)):
            if nums[k] == 1:
                nums[k],nums[i] = nums[i], nums[k]
                i+=1