class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""

        index = set(spaces)
        for i in range(len(s)):
            if i in index:
                ans+=" "
            ans+=s[i]
        return ans