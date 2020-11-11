from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for e in strs:
                if len(e)==i or e[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ''
#         prefix = strs[0]
#         for i in range(1,len(strs)):
#             cnt = 0
#             while True:
#                 if len(prefix)==cnt or len(strs[i])==cnt or prefix[cnt] != strs[i][cnt]:
#                     break
#                 cnt += 1
#             if cnt == 0:
#                 return ''
#             prefix = prefix[:cnt]
#         return prefix

input_list = list(map(str,read().rstrip().split(',')))
mod = Solution()
print(mod.longestCommonPrefix(input_list))
