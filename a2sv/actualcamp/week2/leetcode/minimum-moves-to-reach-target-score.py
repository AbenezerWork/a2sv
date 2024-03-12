class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans =0
        while target>1:
            ans+=target%2
            target-=target%2

            if maxDoubles:
                maxDoubles-=1
                target//=2
                ans+=1
            else:
                ans+=target-1
                break
        return ans
