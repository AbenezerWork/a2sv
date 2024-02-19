class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        ans = 0
        for c in s:
            if c == '0':
                ans+=ones
            else:
                ones+=1
        return ans