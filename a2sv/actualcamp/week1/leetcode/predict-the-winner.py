class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def solve(st, en):
            return nums[en] if st==en else max( nums[st]-solve( st+1, en),  nums[en] - solve( st, en-1) )
        return solve(0, len(nums)-1)>=0
    
