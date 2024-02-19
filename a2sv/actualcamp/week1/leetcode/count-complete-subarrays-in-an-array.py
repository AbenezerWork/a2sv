class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        win = Counter()
        n =  len(set(nums))
        ans = 0
        j = 0
        for i in range(len(nums)):
            win[nums[i]]+=1
            while j<len(nums) and len(win)==n:
                ans += len(nums)-i
                win[nums[j]]-=1
                if win[nums[j]]==0:
                    del(win[nums[j]])
                j+=1

        print(len(win), win)
        return ans
