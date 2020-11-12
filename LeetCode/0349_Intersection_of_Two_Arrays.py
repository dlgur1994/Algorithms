from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         output = []
#         set1 = set(nums1)
#         set2 = set(nums2)
#         for e in set1:
#             if e not in output and e in set2:
#                 output.append(e)
#         return output

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         output = []
#         for e in nums1:
#             if e not in output and e in nums2:
#                 output.append(e)
#         return output

input_list1 = list(map(int,read().rstrip().split(',')))
input_list2 = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.intersection(input_list1, input_list2))
