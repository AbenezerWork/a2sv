class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        dic = set()
        j = 0
        d = 1
        for i in range(len(s)):
            if s[i] not in dic:
                dic.add(s[i])
            else:
                d = max(d, i-j)
                while s[i] in dic:
                    dic.remove(s[j])
                    j+=1
                dic.add(s[i])
        d = max(d, len(s)-j)
        return d
            
