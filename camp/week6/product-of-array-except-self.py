class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = []
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            curr*=nums[i]
            suff.append(curr)
        suff.append(1)
        curr = 1
        ans = []
        print(suff)
        for i in range(len(nums)):
            ans.append(curr*suff[len(nums)-i-2])
            curr*=nums[i]
        return ans