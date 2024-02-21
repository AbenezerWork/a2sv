class Solution:
    def breakPalindrome(self, pal: str) -> str:
        if len(pal)==1:
            return ""
        pal = list(pal)
        for i in range(len(pal)//2):
            if pal[i]!='a':
                pal[i] = 'a'
                return "".join(pal)
        pal[-1] = 'b'
        return "".join(pal)