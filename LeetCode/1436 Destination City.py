from typing import List

import sys
read = sys.stdin.readline

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        intermList = []
        cityList = []

        for i in range(0,int((len(paths)-1)/2)):
            intermList.append(paths[2*i+1])

        buf = intermList
        for i in range(0,int(len(intermList)/2)):
            buf.remove(intermList[2*i])
            if intermList[2*i] not in buf:
                cityList.append(intermList[2*i])
                cityList.append(intermList[2*i+1])
                # intermList.remove(intermList[2*i])
                # intermList.remove(intermList[2*i+1])
            # else:
            #     cityList[i]
            #     intermList -
            #
        return cityList

input = list(read().rstrip().split('"'))
mod = Solution()
result = mod.destCity(input)
print(result)

#[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
