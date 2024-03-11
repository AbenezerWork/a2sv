class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        search = tot%p
        if not search: return 0
        visited = {}
        visited[0] = -1
        tot = 0
        ans = float('inf')
        for i in range(len(nums)):

            tot = (tot+nums[i])%p
            if (tot-search)%p in visited:
                ans = min(ans, i-visited[(tot-search)%p])
            visited[tot] = i
        
        if ans == len(nums):
            return -1
        return ans
