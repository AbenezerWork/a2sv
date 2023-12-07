class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        winners = {}

        for i in matches:
            losers[i[1]] = losers.get(i[1],0)+1
            winners[i[0]] = winners.get(i[0],0)+1
        ans = [[],[]]
        for i in winners:
            if losers.get(i,0)==0:
                ans[0].append(i)
        for i in losers:
            if losers.get(i,0) ==1:
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans
