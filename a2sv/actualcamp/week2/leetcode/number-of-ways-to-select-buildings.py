class Solution:
    def numberOfWays(self, s: str) -> int:
        c1 , c0 = s.count('1'), s.count('0')
        r1 = r0 = 0
        ans = 0
        for i in s:
            if int(i):
                r1+=1
                ans+=r0*(c0-r0)
            else:
                r0+=1
                ans+=r1*(c1-r1)
        return ans
