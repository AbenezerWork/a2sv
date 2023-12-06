class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ans = [0,0]

        mx = -1000000
        mn = float("inf")

        for i in nums:
            if mx>i:
                ans[0]+=1
            mx = max(i,mx)
        for i in nums[::-1]:
            if mn < i:
                ans[1]+=1
            mn = min(i,mn)
        return ans[0]<2 or ans[1]<2