class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans =[]
        def recc(i,curr):
            if i == len(nums):
                self.ans.append(curr[:])
                return 
            
            curr.append(nums[i])
            recc(i+1, curr)
            curr.pop()
            recc(i+1, curr)
            
        recc(0,[])
        return self.ans
