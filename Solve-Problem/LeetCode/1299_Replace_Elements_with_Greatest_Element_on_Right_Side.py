from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2,-1,-1):
            arr[i] = max(arr[i],arr[i+1])
        return arr[1:] + [-1]

        # output = []
        #
        # for i in range(0,len(arr)-1):
        #     arr[i] = 0
        #     output.append(max(arr))
        # output.append(-1)
        #
        # return output

input = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.replaceElements(input))
