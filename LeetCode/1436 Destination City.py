from typing import List

import sys
read = sys.stdin.readline

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityList = []
        for e in paths:
            #cityList.append(e.split(','))
            print(e)
        return cityList

#[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]


input = read().rstrip()
#list(read().rstrip().split(','))
mod = Solution()
result = mod.destCity(input)
print(result)
