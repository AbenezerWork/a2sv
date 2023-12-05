class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = 0
        for i in candies:
            mx = max(mx, i)
        res = []
        for i in candies:
            if i+extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        return res
