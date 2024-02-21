class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1
        s = set()
        for i in rolls:
            s.add(i)
            if len(s)==k:
                s = set()
                ans+=1
        return ans