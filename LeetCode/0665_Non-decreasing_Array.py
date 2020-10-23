from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        for i in range(len(nums)):
            temp = nums[:]
            del temp[i]
            print(temp)
            if temp == sorted(temp):
                return True
        return False

num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.checkPossibility(num_list))

#얕은 복사, del temp[i]
