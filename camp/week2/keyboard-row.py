class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        check = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        ans = []
        for word in words:
            i = 0
            wordl = word.lower()
            exists = True
            if wordl[0] in check[0]:
                i = 0
            elif wordl[0] in check[1]:
                i = 1
            else:
                i =2
            for ch in wordl:
                if ch not in check[i]:
                    exists = False
            if exists:
                ans.append(word)

        return ans