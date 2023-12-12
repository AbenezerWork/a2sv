class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            dic[nums[i]]=(i)