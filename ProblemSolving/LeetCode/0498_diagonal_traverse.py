import sys
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        for row in range(len(mat)):
            col = 0
            while row > -1:
                result.append(mat[row][col])
                row -= 1
                col += 1
        for col in range(1, len(mat)):
            row = 0
            while col < len(mat):
                result.append(mat[row][col])
                row -= 1
                col += 1
        return result

matrix = []
rows = list(sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split('],['))
for row in rows:
    matrix.append(list(map(int, row.split(','))))
mod = Solution()
print(mod.findDiagonalOrder(matrix))