from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_dict = {}
        for i, e in enumerate(numbers):
            if target-e in val_dict.keys():
                return [val_dict[target-e], i+1]
            val_dict[e] = i+1

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)-1):
#             if target-numbers[i] in numbers and numbers.index(target-numbers[i]) != i:
#                 return [min(i+1, numbers.index(target-numbers[i])+1), max(i+1, numbers.index(target-numbers[i])+1)]

input_num = list(map(int,read().rstrip().split(',')))
input_tar = int(read().rstrip())
mod = Solution()
print(mod.twoSum(input_num, input_tar))
