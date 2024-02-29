class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.solve(nums, 1, 0, len(nums)-1)>=0

    def solve(self, nums, t, st, en):
        if st == en:
            return t*nums[en]

        left = self.solve(nums, t*-1, st+1, en)+t*(nums[st])
        right = self.solve(nums, t*-1, st, en-1)+ t*(nums[en])

        if t == 1:
            return max(left, right)
        else:
            return min(left, right)
