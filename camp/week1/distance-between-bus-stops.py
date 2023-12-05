class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dist1 = 0
        total = 0
        for i in range(len(distance)):
            if i < max(start, destination) and i>=min(start, destination):
                dist1+=distance[i]
            total += distance[i]

        return min(total-dist1, dist1)