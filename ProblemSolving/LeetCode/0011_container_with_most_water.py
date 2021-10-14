import sys
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_num = 0
        for i in range(len(height)-1):
            for j in range((len(height), i+1), -1):
                temp = (j-i) * min(height[i], height[j])
                max_num = max(max_num, temp)
        return max_num

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_num = 0
#         for i in range(len(height)-1):
#             for j in range(i+1, (len(height))):
#                 temp = (j-i) * min(height[i], height[j])
#                 max_num = max(max_num, temp)
#         return max_num

height = list(map(int, sys.stdin.readline().rstrip().split(',')))
mod = Solution()
print(mod.maxArea(height))