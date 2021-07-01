from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in num_dict:
                return num_dict[target-nums[i]],i
            else:
                num_dict[nums[i]] = i

num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
target_num = int(read().rstrip())
mod = Solution()
print(mod.twoSum(num_list,target_num))
