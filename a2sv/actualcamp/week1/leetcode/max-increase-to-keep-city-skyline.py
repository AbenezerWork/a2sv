class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mr = [0]*len(grid)
        mc = [0]*len(grid)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                mr[i] = max(mr[i],grid[i][j])
                mc[j] = max(mc[j],grid[i][j])
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans+=min(mr[i],mc[j])-grid[i][j]
        return ans
        


