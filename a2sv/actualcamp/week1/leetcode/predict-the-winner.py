class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        res = self.solve(nums, 1, 0, len(nums)-1)
        return res[0]<=res[1]


    def solve(self, nums, turn, start, end):
        
        if start == end:
            if turn % 2:
                return [0, nums[start]]
            else:
                return [nums[start], 0]

        left = self.solve(nums,turn+1,start+1,end)
        right = self.solve(nums,turn+1,start,end-1)
        if turn % 2:
            if left[1]+nums[start]-left[0]>=right[1]+nums[end]-right[0]:
                left[1]+=nums[start]
                return left
            else:
                right[1]+=nums[end]
                return right
        else:
            if left[0]+nums[start]-left[1]>right[0]+nums[end]-right[1]:
                left[0]+=nums[start]
                return left
            else:
                right[0]+=nums[end]
                return right

