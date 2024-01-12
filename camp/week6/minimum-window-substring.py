class Solution:
    def inWin(self,win:defaultdict, tar:defaultdict):
        for k in tar:
            if tar[k]>win[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        j = 0
        m = defaultdict(int)
        d = defaultdict(int)
        mx = [float("inf"),0]
        for c in t:
            d[c]+=1
        for i in range(len(s)):
            m[s[i]]+=1
            while j<=i and self.inWin(m,d):
                mx = [i,j] if mx[0]-mx[1]>i-j else mx
                m[s[j]]-=1
                if m[s[j]]==0:
                    del(m[s[j]])
                j+=1
        if mx[0]==float("inf"):
            return ''

        return s[mx[1]:mx[0]+1]