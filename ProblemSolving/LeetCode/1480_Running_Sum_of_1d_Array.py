from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        output_list = []

        for num in nums:
            sum += int(num)
            output_list.append(sum)
        return output_list

input_list = read().rstrip()
mod = Solution()
print(mod.runningSum(input_list))
