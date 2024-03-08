class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cumm = []
        ans = []
        candidates.sort()
        def rec (idx):
            if sum(cumm) >= target:
                if sum(cumm) == target:
                    ans.append(cumm[:])
                else: return
                
            
            for i in range(idx, len(candidates)):
                cumm.append(candidates[i])
                rec(i)
                cumm.pop()
        rec(0)
        return ans
                    

