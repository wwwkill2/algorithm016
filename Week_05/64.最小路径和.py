class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        bp = [None for _ in range(n)]
        for i in range(n):
            if i == 0:
                bp[i] = grid[0][i]
            else:
                bp[i] = bp[i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    bp[j] += grid[i][j]
                else:
                    bp[j] = grid[i][j] + min(bp[j], bp[j-1])
        return bp[-1]
