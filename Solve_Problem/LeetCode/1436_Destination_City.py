from typing import List

import sys
read = sys.stdin.readline

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startList = [path[0] for path in paths]
        destList = [path[1] for path in paths]
         
        for e in startList:
            if e in destList:
                destList.remove(e)
        
        return destList[0]

# input = list(read().rstrip().split('"'))
input = read()
print(input)
mod = Solution()
result = mod.destCity(input)
print(result)

#[["Lima","Sao Paulo"],["London","New York"],["New York","Lima"]]
