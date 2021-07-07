from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            for e in row:
                if e<0:
                    count += len(row)-row.index(e)
                    break

        return count

input_matrix = read().rstrip().lstrip('[[').rstrip(']]').split('],[')
refined_matrix = [[int(e) for e in row.split(',') ]for row in input_matrix]
mod = Solution()
print(mod.countNegatives(refined_matrix))
