class UndergroundSystem:

    def __init__(self):
        self.map = defaultdict(int)
        self.times = defaultdict(int)
        self.visits = defaultdict(int)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.times[(self.map[id][0], stationName)] +=t-self.map[id][1]
        self.visits[(self.map[id][0], stationName)] +=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)]/self.visits[(startStation,endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)