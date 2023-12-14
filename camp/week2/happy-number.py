class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while True:
            string = str(n)
            if n in check or n==1:
                return '1'==string
            sum = 0
            for c in string:
                sum+=int(c)**2
            check.add(n)
            n=sum
            