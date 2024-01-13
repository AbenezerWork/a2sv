class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = "aeiou"
        count =ans = 0
        for i in range(len(s)):
            if s[i] in d:
                count+=1
            if i>=k:
                if s[i-k] in d:
                    count-=1
            ans = max(ans,count)
        return ans