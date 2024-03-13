class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        def recc(curr, num):
            if sum(curr)>=n or num>9:
                if sum(curr) == n and len(curr) == k:
                    self.ans.append(curr[:])
                return 
            curr.append(num)
            recc(curr, num+1)
            curr.pop()
            recc(curr, num+1)
        recc([], 1)
        return self.ans
