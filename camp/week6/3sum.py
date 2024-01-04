class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)-2):
            left = i+1
            diff = 0-nums[i]
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right] == diff:
                    ans.add(tuple([nums[i],nums[left],nums[right]]))
                    left+=1
                    right-=1
                if nums[left]+nums[right]<diff:
                    left+=1

                if nums[left]+nums[right]>diff:
                    right-=1
        return list(ans)
                