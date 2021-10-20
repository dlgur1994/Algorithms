import sys
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        row, col = 0, 0
        dir = 'up'
        while len(result) < len(mat)*len(mat[0]):
            if row>-1 and row<len(mat) and col>-1 and col<len(mat[0]):
                result.append(mat[row][col])
            if dir == 'up':
                row -= 1
                col += 1
            else:
                row += 1
                col -= 1
            if row == -1:
                dir = 'up'
            else:
                dir = 'down'
        return result

# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         result = [mat[0][0]]
#         dir = 'down'
#         for i in range(1,len(mat)+len(mat[0])-1):
#             for j in range(i+1):
#                 if dir == 'down':
#                     if j<len(mat) and i-j<len(mat[0]):
#                         result.append(mat[j][i-j])
#                 else:
#                     if i-j<len(mat) and j<len(mat[0]):
#                         result.append(mat[i-j][j])
#             dir = 'up' if dir=='down' else 'down'
#         return result

matrix = []
rows = list(sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split('],['))
for row in rows:
    matrix.append(list(map(int, row.split(','))))
mod = Solution()
print(mod.findDiagonalOrder(matrix))