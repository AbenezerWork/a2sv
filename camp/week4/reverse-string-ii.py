class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = k*2
        ans = list(s)
        end = 0
        for i in range(0,len(s),k*2):
            end = i+k
            ans[i:end] = reversed(ans[i:end])
        return ''.join(ans)

