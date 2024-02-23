class Solution:
    def minFlips(self, target: str) -> int:
        check = '0'
        ans = 0
        for i in target:
            if i!= check:
                ans+=1
                check = i
        return ans