class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = -1, len(nums)

        while l+1<r:
            mid = l+(r-l)//2
            if target>nums[mid]:
                l = mid
            else:
                r = mid

        if l+1>= len(nums) or nums[l+1]!=target:
            return [-1,-1]

        ans = [l+1,0]
        l,r = -1, len(nums)

        while l+1<r:
            mid = l+(r-l)//2
            if target>=nums[mid]:
                l = mid
            else:
                r = mid
        ans[1] = l
        return ans