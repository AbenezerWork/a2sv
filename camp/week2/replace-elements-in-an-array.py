class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = i

        ans = nums

        for op in operations:
            dic[op[1]] = dic[op[0]]
            ans[dic[op[1]]] = op[1]             

        return ans