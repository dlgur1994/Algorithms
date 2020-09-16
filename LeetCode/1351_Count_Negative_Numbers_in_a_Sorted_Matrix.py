from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            for column in row:
                if column<0:
                    count += len(row)-column
                    break

        return count

input_matrix = list(map(int,read().rstrip()))
mod = Solution()
print(mod.countNegatives(input_matrix))
