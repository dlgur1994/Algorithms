from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        if len(nums)<3:
            return True
        for i in range(1, len(nums)-1):
            if nums[i]>nums[i+1]:
                cnt += 1
                nums[i]=nums[i+1]


num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.checkPossibility(num_list))

#얕은 복사, del temp[i]
