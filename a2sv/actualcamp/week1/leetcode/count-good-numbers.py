class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = n//2 + n%2
        odd = n//2
        return ((self.power(5,even))*(self.power(4,odd)))%(10**9+7)
    def power(self, n, m):
        if m == 1:
            return n

        if m == 0:
            return 1
        
        left = m//2
        edge = 1

        if m%2:
            edge = n
        return ((self.power(n,left)**2)*edge)%(10**9+7)