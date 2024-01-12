class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        z = 0
        mx = 0
        for i in range(len(nums)):
            if not nums[i]:
                z+=1
            while z>k:
                if not nums[j]:
                    z-=1
                j+=1
            mx = max(mx,i-j+1)
        return mx