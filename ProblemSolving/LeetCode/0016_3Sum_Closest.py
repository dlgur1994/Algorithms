import sys
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = sum(nums[0:3]) 

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target-ans) > abs(temp-target):
                    ans = temp
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
                else:
                    return ans

        return ans

        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             temp = nums[i] + nums[j] + nums[k]
        #             if abs(target-ans) > abs(temp-target):
        #                 ans = temp
        #             if abs(target-ans) < temp-target:
        #                 break
        # return ans

nums = list(map(int, sys.stdin.readline().rstrip().split(',')))
target = int(sys.stdin.readline().rstrip())
mod = Solution()
print(mod.threeSumClosest(nums, target))