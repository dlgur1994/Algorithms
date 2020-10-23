from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[nums1.index(0)] = nums2[i]
        nums1.sort()
        print(nums1)

num_list1 = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
num1 = int(read().rstrip())
num_list2 = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
num2 = int(read().rstrip())
mod = Solution()
mod.merge(num_list1, num1, num_list2, num2)
