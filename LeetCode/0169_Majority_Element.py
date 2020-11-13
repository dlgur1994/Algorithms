from typing import List
from collections import Counter
import sys
read = sys.stdin.readline

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        half = len(nums)//2
        for e in counts:
            if counts[e] > half:
                return e

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return Counter(nums).most_common(1)[0][0]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cnt_dict = {}
#         for e in nums:
#             if e not in cnt_dict:
#                 cnt_dict[e] = 1
#             else:
#                 cnt_dict[e] += 1
#                 if cnt_dict[e] > len(nums)//2:
#                     return e
#         return max(cnt_dict, key = lambda x : cnt_dict[x])

input_list = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.majorityElement(input_list))
