class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = [nums[0]]

        for i in nums[1:]:
            sum.append(sum[-1]+i)
    
        return sum