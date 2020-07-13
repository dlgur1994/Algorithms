from typing import List

import sys
read = sys.stdin.readline

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        intermList = []
        cityList = []

        for i in range(0,int((len(paths)-1)/2)):
            intermList.append(paths[2*i+1])

        for i in range(0,len(intermList)):
            if i%2 == 1:
                for


        return cityList

input = list(read().rstrip().split('"'))
mod = Solution()
result = mod.destCity(input)
print(result)

#[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
