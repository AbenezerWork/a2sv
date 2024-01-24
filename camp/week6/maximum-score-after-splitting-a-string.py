class Solution:
    def maxScore(self, s: str) -> int:
        suff = [0]
        pref = [0]
        for c in s:
            if c == '0':
                pref.append(pref[-1]+1)
            else:
                pref.append(pref[-1])
        for c in s[::-1]:
            suff.append(suff[-1]+int(c))
        print(suff,pref)
        mx = 0
        for i in range(1,len(suff)-1):
            mx = max(mx,pref[i]+suff[len(suff)-i-1])
        return mx