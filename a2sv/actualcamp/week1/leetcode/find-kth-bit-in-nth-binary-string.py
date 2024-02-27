class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.solve(n,k)%2)
    
    def solve(self, n,k):
        if n == 1:
            return 0
        mid = (2**n)//2
        if k==mid:
            return 1
        elif k<mid: 
            return self.solve(n-1,k)
        else:
            t = (mid-1)-(k-1-mid)
            return self.solve(n-1,t)+1