class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def solve(t,st, en):
            if st == en:
                return t*nums[en]
    
            left = solve( t*-1, st+1, en)+ t*(nums[st])
            right = solve(t*-1, st, en-1)+ t*(nums[en])
    
            if t == 1:
                return max(left, right)
            else:
                return min(left, right)
        return solve( 1, 0, len(nums)-1)>=0
    
