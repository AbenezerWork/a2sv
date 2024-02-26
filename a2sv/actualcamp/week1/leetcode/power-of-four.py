class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.solve(n)
    def solve(self,n):
        if n<1:
            return False
        if n==1:
            return True
        return self.solve(n/4)