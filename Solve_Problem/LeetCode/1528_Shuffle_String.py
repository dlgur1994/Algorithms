from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = [""] * len(indices)
        for i, index in enumerate(indices):
            new_str[index] = s[i]
        return "".join(new_str)

# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         str_dict = {}
#         cnt = 0
#         new_str = ''
#         for indice in indices:
#             str_dict[indice] = s[cnt]
#             cnt += 1
#         for i in range(len(str_dict)):
#             new_str += str_dict[i]
#         return new_str

input_str = read().rstrip()
input_list = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.restoreString(input_str, input_list))
