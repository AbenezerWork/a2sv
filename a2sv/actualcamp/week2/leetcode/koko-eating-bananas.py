class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if len(piles)==1:
        #    return ceil(piles[0]/h)
        def checker(n):
            curr = ans = 0
            i = 0
            for i in range(len(piles)):
                ans+=ceil(piles[i]/n)
                if ans>h:
                    return False
            return True
        
        high = 1e9
        low = 0
        while low+1<high:
            mid = low+(high-low)//2
            if checker(mid):
                high = mid
            else: 
                low = mid
        return int(high)

        