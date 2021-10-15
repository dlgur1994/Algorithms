import sys
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        head, tail = 0, len(height)-1
        while head < tail:
            area = (tail-head) * min(height[head], height[tail])
            max_area = max(max_area, area)
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        return max_area

# Time Limit Exceeded
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