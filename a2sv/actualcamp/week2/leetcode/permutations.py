class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.v = set()
        def recc(curr):
            if len(curr)==len(nums):
                self.ans.append(curr[:])
                return 
            for i in range(len(nums)):
                if nums[i] not in self.v:
                    curr.append(nums[i])
                    self.v.add(nums[i])
                    recc(curr)
                    curr.pop()
                    self.v.remove(nums[i])
        recc([])
        return self.ans
            