class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        distance = 0
        for point in points[1:]:
            distance+=max(abs(prev[0]-point[0]),abs(prev[1]-point[1]))
            prev = point
        return distance