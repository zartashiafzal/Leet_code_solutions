class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfsFill(grid, i, j)
                    count += 1
        return count

    def dfsFill(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfsFill(grid, i + 1, j)
            self.dfsFill(grid, i - 1, j)
            self.dfsFill(grid, i, j + 1)
            self.dfsFill(grid, i, j - 1)




# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # Check if the grid is empty
#         if not grid or not grid[0]:
#             return 0

#         # Initialize variables
#         islands = 0
#         visit = set()
#         rows, cols = len(grid), len(grid[0])

#         def dfs(r, c):
#             # Base cases for DFS recursion
#             if (
#                 r not in range(rows)
#                 or c not in range(cols)
#                 or grid[r][c] == "0"
#                 or (r, c) in visit
#             ):
#                 return

#             # Mark the current cell as visited
#             visit.add((r, c))

#             # Define directions (right, left, down, up)
#             directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#             # Explore neighbors recursively
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)

#         # Iterate through each cell in the grid
#         for r in range(rows):
#             for c in range(cols):
#                 # Check if the cell is land and not visited
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     # Start a new island and perform DFS to mark connected land cells
#                     islands += 1
#                     dfs(r, c)

#         return islands













# BFS Version
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        # Initialize variables
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            # Initialize a queue for BFS
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            # Explore neighbors using BFS
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check if the neighbor is within bounds, is land, and not visited
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        # Enqueue the neighbor and mark it as visited
                        q.append((nr, nc))
                        visited.add((nr, nc))

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Check if the cell is land and not visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Start a new island and perform BFS to mark connected land cells
                    islands += 1
                    bfs(r, c)

        return islands
