class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = Counter(s)
        ans = 0
        odd = 0
        for c in check.keys():
            if check[c]%2:
                odd+=1
                ans+=check[c]-1
            else:
                ans+=check[c]
        if odd:
            ans+=1
        return ans
