from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        if len(nums)<3:
            return True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if cnt>0:
                    return False
                cnt += 1
                if i>0 and nums[i-1]>nums[i+1]:
                    nums[i+1] = nums[i]
        return True

num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.checkPossibility(num_list))

#얕은 복사, del temp[i]
