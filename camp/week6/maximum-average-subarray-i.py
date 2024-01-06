class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = 0
        i , j = 0, 0
        maxSum = -float("inf")
        while j<len(nums):
            if j<k:
                while j<k:
                    sm+=nums[j]
                    j+=1
                maxSum = max(sm, maxSum)
            else:
                sm-=nums[i]
                sm+=nums[j]
                maxSum = max(sm, maxSum)
                i+=1
                j+=1
        return maxSum/k
            