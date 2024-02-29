class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x,n):
            if n==1:
                return x
            elif n == -1:
                return 1/x
            elif n == 0:
                return 1
            ex = 1
            if n%2:
                ex = x
            fac = n//2
            #print((rec(x, n//2)**2)*ex)
            return (rec(x, n//2)**2)*ex
        ans =  rec(x,n)
        if n<0:
            return ans
        else:
            return ans
            
