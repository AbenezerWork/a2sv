class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(r):
            j = 0
            for i in range(len(houses)):
                if abs(heaters[j]-houses[i]) > r:
                    j+=1
                    while j<len(heaters) and abs(heaters[j]-houses[i])>r:
                        j+=1
                    if j>=len(heaters):
                        return False

            return True

        
        l, r = -1, int(1e18)
        while l+1<r:
            mid = l + (r-l)//2
            if checker(mid):
                #print(mid)
                r = mid
            else:
                l = mid
        return r
