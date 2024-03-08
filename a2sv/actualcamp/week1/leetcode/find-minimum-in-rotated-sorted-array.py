class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:return nums[0]
        low , high = 0, len(nums)-1
        an = 0
        while low+1<high:
            mid = low+(high-low)//2
            if nums[mid]<nums[high]:
                high = mid
                an = mid
            else:
                low = mid
        return nums[high]