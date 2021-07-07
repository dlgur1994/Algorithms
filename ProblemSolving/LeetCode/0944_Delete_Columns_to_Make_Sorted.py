from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def minDeletionSize(self, A):
        count = 0
        # The * operator was used to unzip the list.
        for items in zip(*A):
            if sorted(items) != list(items):
                count += 1
        return count

# class Solution:
#     def minDeletionSize(self, A: List[str]) -> int:
#         out_list = []
#         for i in range(len(A[0])):
#             for j in range(len(A)-1):
#                 if A[j][i] > A[j+1][i]:
#                     out_list.append(i)
#                     break
#         return len(out_list)

input_list = list(read().rstrip().split(','))
mod = Solution()
print(mod.minDeletionSize(input_list))
