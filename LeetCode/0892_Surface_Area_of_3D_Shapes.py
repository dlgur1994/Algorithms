from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        return 0

inputs = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
grid = []
for e in inputs:
    grid.append(list(map(int, e.split(','))))
print(grid)
mod = Solution()
print(mod.surfaceArea(grid))
