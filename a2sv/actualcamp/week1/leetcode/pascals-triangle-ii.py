class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]
        self.solve(rowIndex,nums)
        return nums
        
    def solve(self, n, nums):
        if n == 0:
            return
        self.solve(n-1, nums)
        curr = nums.copy()
        nums.append(1)
        for i in range(len(curr)//2):
            nums[i+1]=nums[len(nums)-2-i]=curr[i]+curr[i+1]
        
