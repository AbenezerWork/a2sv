class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.solve(n-1, k)%2

    def solve(self,n,k):
        if n == 0:
            return 0
        
        if k >2**(n-1):
            return self.solve(n-1, k - 2**(n-1))+1
        else:
            return self.solve(n-1,k)
        