class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(c):
            curr=ans=0
            for i in range(len(weights)):
                if weights[i]>c:
                    return False
                if curr+weights[i]<=c:
                    curr+=weights[i]
                else: 
                    ans+=1
                    curr = weights[i]
                if ans>days:
                    return False
            if curr:
                ans+=1
            return ans<=days

        low = 0
        high = sum(weights) + 1
        sm = high
        print(sm)
        while low+1<high:
            mid = (high+low)//2
            print(mid)
            if checker(mid):
                high = mid
            else:
                low = mid
        print(low,high)
        return high