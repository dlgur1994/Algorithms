from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def rotate(self, matrix: list) -> None:
        l = len(matrix)-1
        for i in range(len(matrix)//2): # the number of edges
            for j in range(i, len(matrix[0])-i-1): # the number of times an array must be rotated from that edge
                # the rotating elements change continuously
                temp = matrix[i][j]
                matrix[i][j] = matrix[l-j][i]
                matrix[l-j][i] = matrix[l-i][l-j]
                matrix[l-i][l-j] = matrix[j][l-i]
                matrix[j][l-i] = temp

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         nums = []
#         cnt = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 nums.append(matrix[i][j])
#         for i in range(len(matrix[0])-1,-1,-1):
#             for j in range(len(matrix)):
#                 matrix[j][i] = nums[cnt]
#                 cnt += 1

temp = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
matrix = []
for e in temp:
    matrix.append(list(map(int,e.split(','))))
mod = Solution()
mod.rotate(matrix)
print(matrix)
