class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = mx = l = 0
        st = defaultdict(int)

        for r in range(len(s)):
            st[s[r]]+=1
            mx = max(st[s[r]],mx)

            while mx+k<r-l+1:
                st[s[l]]-=1
                l+=1
            ans = max(r-l+1,ans)
            
        
        return ans