class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def recc(first_num, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            for i in range(first_num, n+1):
                curr.append(i)
                recc(i+1, curr)
                curr.pop()
        recc(1, [])
        return ans