class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.times = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.times[tokenId]=currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.times[tokenId] > currentTime:
            self.times[tokenId] = currentTime+self.ttl
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for value in self.times.values():
            if value > currentTime:
                count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)