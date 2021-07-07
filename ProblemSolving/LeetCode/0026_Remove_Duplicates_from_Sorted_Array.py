from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        cnt = 0
        for i,e in enumerate(nums):
            if e not in num_dict.keys():
                num_dict[e] = i
                nums[cnt] = e
                cnt += 1
        return cnt

input_list = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.removeDuplicates(input_list))
