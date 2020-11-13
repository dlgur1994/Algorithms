from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)):
            if nums[i]>0:
                temp = 0
                for j in range(i,len(nums)):
                    temp += nums[j]
                    max = temp if temp > max else max
            else:
                max = nums[i] if nums[i] > max else max
        return max

input_list = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.maxSubArray(input_list))
