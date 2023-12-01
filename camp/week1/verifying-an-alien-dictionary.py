class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hsh = {}
        for i in range(26):
            hsh[order[i]] = i+1
        
        mx = 0
        arr = []
        length = 0
        for word in words:
            length = max(length, len(word))
        for string in words:
            val = 0
            dig = length-1
            for ch in string:
                val+=hsh[ch]*26**dig
                dig-=1
            arr.append(val)
        print arr

        for i in arr:
            if mx > i:
                return False
            mx = max(mx, i)


        return True


            

        