class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cumm = []
        candidates.sort()
        def recc(idx):
            if sum(cumm)>=target:
                if sum(cumm)==target:
                    ans.append(cumm[:])
                else:
                    return
            prev = -1
            for i in range(idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                cumm.append(candidates[i])
                recc(i+1)
                cumm.pop()
                prev = candidates[i]
        recc(0)
        return ans