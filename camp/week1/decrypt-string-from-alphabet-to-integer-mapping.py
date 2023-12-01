class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        base = ord('a')
        curr = ''
        ans = ''
        for ch in s:
            if ch != '#':
                curr+=ch
            else:
                re = 0
                while len(curr)-re>2:
                    ans+=chr(int(curr[re])-1+base)
                    re+=1
                    
                ans += chr(int(curr[re:])-1+base)
                curr = ""
        for c in curr:
            ans+=chr(int(c)-1+base)
            
        return ans
        