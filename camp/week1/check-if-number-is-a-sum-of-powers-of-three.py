class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        res = []
        while 3**x<=n:
            res.append(3**x)
            x+=1

        res = res[::-1]

        ans = 0

        for i in res:
            ans+=i
            if ans>n:
                ans-=i

        return ans==n
        

        