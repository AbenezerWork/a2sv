class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i=j = 0
        n,m = len(players),len(trainers)
        players.sort()
        trainers.sort()
        ans=0
        while i<n and j<m:
            if players[i]>trainers[j]:
                j+=1
            else:
                i+=1
                j+=1
                ans+=1
        return ans