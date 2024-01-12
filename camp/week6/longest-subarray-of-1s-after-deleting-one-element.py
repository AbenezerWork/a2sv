class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j=0
        Del = False
        mx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if Del:
                    while nums[j]:
                        j+=1
                    j+=1
                else:
                    Del = True
            mx = max(mx, i-j)
        return mx

            
            