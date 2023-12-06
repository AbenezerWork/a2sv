class Solution:
    def totalMoney(self, n: int) -> int:
        return int((n//7)*28 + ((2*(n//7-1)+(n//7-1)*(n//7-2))/2)*7 + ((2*(n%7)+(n%7)*(n%7-1))/2)+ ((n//7)*(n%7)))
    
