class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(n):
            tot = 0
            for i in range(len(nums)):
                tot+=(nums[i]+n-1)//n
            return tot<=threshold
        l,r = 0,int(1e7)
        while l+1<r:
            mid = l+(r-l)//2
            if checker(mid):
                r = mid
            else:
                l = mid
        return r