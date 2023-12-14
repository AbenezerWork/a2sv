class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dic = set()
        for c in s:
            dic.add(c)
        return len(dic)
