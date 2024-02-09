class Solution:
    def balancedString(self, s: str) -> int:
        ans = n = len(s)
        win = Counter(s)

        l = 0
        for r in range(n):
            win[s[r]]-=1
            while l<n and all(win[c]<=n/4 for c in "QWER"):
                ans = min(ans, r-l+1)
                win[s[l]]+=1
                l+=1
            print(win)
        return ans