from typing import List

import sys
read = sys.stdin.readline

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startList = []
        destList = []
        cityList = []

        #separate start points and destinations
        for i in range(0,int((len(paths))/4)):
            startList.append(paths[4*i+1])
            destList.append(paths[4*i+3])

        for i in range(0,len(startList)):
            if startList[i] not in destList:
                cityList.append(startList[i])
                cityList.append(destList[i])

        return cityList

input = list(read().rstrip().split('"'))
mod = Solution()
result = mod.destCity(input)
print(result)

#[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
