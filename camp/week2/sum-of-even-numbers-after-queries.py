class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        ans = []
        for num in nums:
            if not num%2:
                even+=num

        for query in queries:
            i = query[1]
            val = query[0]
            if not nums[i]%2:
                even-=nums[i]
            nums[i]+=val
            if not nums[i]%2:
                even+=nums[i]
            ans.append(even)
        return ans