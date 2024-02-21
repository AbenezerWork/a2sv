class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        ans = 0
        print(points)
        end = -float("inf")
        for i in range(len(points)):
            if end<points[i][0]:
                ans +=1
                end = points[i][1]
            else:
                end = min(points[i][1],end)
        return ans