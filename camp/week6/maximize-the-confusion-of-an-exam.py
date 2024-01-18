class Solution:
    def maxConsecutiveAnswers(self, s: str, ko: int) -> int:
        ans =0
        for c in "TF":
            k = ko
            j=0
            for i in range(len(s)):
                if s[i] == c:
                    k-=1
                while k<0:
                    if s[j] == c:
                        k+=1
                    j+=1
                ans = max(ans,i-j+1)
        return ans
