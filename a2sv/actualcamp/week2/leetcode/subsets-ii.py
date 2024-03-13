class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recc(idx, curr):
            if idx == len(nums):
                self.ans.append(tuple(sorted(curr)))
                return 
            
            curr.append(nums[idx])
            recc(idx+1, curr)
            curr.pop()
            recc(idx+1,curr)
        recc(0,[])
        return set(self.ans)