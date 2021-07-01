from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check_dict = {}
        for e in nums:
            if e not in check_dict:
                check_dict[e] = 1
            else:
                del check_dict[e]
        return list(check_dict.keys())[0]

input_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.singleNumber(input_list))
