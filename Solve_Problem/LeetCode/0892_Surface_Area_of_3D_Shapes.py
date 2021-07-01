from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bottom = 0
        row = 0
        col = 0
        for i in range(n):
            for j in range(n):
                # If a block exists, there are upper and lower sides. Therefore, add 1 to the width of the lower face and eventually double the area of the lower face to obtain the area of the upper and lower sides.
                if grid[i][j] > 0:
                    bottom += 1

                # Obtain the area of the first and last rows.
                if i==0 or i==n-1:
                    if j==0 or j==n-1:
                        row += grid[i][j]
                    col += grid[i][j]

                # Obtain the side area of the blocks except the first and last blocks of both sides.
                if j==0 or j==n-1:
                    if i>0 and i<n-1:
                        row += grid[i][j]

                # Both side areas can be obtained by the difference between the number of blocks in the next space.
                if j>0 and j<n:
                    row += abs(grid[i][j] - grid[i][j-1])

                # The area of the front and back is obtained by the difference between the number of blocks in the next space.
                if i>0 and i<n:
                    col += abs(grid[i][j] - grid[i-1][j])

        # If the length of the grid is 1, double the width of the front, back, and sides.
        if n == 1:
            row *= 2
            col *= 2
        return bottom*2 + row + col

inputs = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
grid = []
for e in inputs:
    grid.append(list(map(int, e.split(','))))
mod = Solution()
print(mod.surfaceArea(grid))
