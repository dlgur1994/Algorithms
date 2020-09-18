from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for i in range(0,len(A[0])):
                row[i] ^= 1
        return A

# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
#         for i in range(0, len(A)):
#             for j in range(0,int(len(A[0])/2)):
#                 A[i][j], A[i][len(A[0])-1-j] = A[i][len(A[0])-1-j], A[i][j]
#
#         for i in range(0, len(A)):
#             for j in range(0,len(A[0])):
#                 if A[i][j] == 0:
#                     A[i][j] = 1
#                 else:
#                     A[i][j] = 0
#         return A

input_matrix = read().rstrip().lstrip('[[').rstrip(']]').split('],[')
refined_input_matrix = [[int(e) for e in row.split(',')] for row in input_matrix]
mod = Solution()
print(mod.flipAndInvertImage(refined_input_matrix))
