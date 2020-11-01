class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                DFS(i-1, j)
                DFS(i+1, j)
                DFS(i, j-1)
                DFS(i, j+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    DFS(i, j)
        return count
