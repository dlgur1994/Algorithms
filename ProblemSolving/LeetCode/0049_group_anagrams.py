import sys
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dic = dict()
        for e in strs:
            temp = ''.join(sorted(e))
            if temp in ana_dic:
                ana_dic[temp].append(e)
            else:
                ana_dic[temp] = [e]
        return list(ana_dic.values())

strs = list(sys.stdin.readline().rstrip().split(','))
mod = Solution()
print(mod.groupAnagrams(strs))