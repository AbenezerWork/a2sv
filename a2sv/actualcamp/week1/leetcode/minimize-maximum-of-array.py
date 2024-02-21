class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = 0
        sm = 0
        for i in range(0,len(nums)):
            sm+=nums[i]
            mx = max(ceil(sm/(i+1)), mx)

        return int(mx)
