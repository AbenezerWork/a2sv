class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j = 0
        curr=count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]%2:
                curr+=nums[i]%2
                count=0
            while curr==k:
                curr-=nums[j]%2
                count+=1
                j+=1
            ans+=count
        return ans