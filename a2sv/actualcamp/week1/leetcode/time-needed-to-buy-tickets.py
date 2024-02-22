class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        mn = tickets[k]
        ans = 0
        print(tickets[k])
        for i in range(len(tickets)):
            t = tickets[i]
            if i>k and mn<=t:
                ans+=min(t,mn-1)
            else:
                ans+=min(t,mn)
        return ans