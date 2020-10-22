from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = { i: nums[i] for i in range(len(nums))}
        print(num_dict)
        # for e in nums:
        #     if (target-e) in nums:
        #         nums2 = list(reversed(nums))
        #         if nums.index(e)==len(nums)-1-nums2.index(target-e):
        #             continue
        #         return [nums.index(e),len(nums)-1-nums2.index(target-e)]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
target_num = int(read().rstrip())
mod = Solution()
print(mod.twoSum(num_list,target_num))
