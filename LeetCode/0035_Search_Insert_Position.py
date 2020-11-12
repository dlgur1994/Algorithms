from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i


input_list = list(map(int,read().rstrip().split(',')))
input_val = int(read().rstrip())
mod = Solution()
print(mod.searchInsert(input_list, input_val))
