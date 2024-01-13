class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        s = defaultdict(int)
        j = 0
        mn = float('inf')
        for i in range(len(nums)):
            if s[nums[i]]:
                while nums[j]!=nums[i]:
                    s[nums[j]]-=1
                    j+=1
                if i-j+1>1:
                    mn = min(i-j+1,mn)
                    j+=1
            s[nums[i]]+=1


        return mn if mn<=len(nums) else -1