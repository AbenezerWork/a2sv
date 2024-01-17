class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap = [0]*1001
        mx = 0
        for p in trips:
            cap[p[1]]+=p[0]
            cap[p[2]]-=p[0]
            mx = max(p[2],mx)
        mc =sum = 0
        for i in range(mx):
            sum+=cap[i]
            if sum>capacity:
                return False
        return True
        