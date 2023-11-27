#from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    break
        return self.count
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            self.count += 1
            return
        if grid[i][j] == -1:
            return

        grid[i][j] = -1

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
