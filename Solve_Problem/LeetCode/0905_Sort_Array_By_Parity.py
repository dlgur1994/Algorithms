from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [e for e in A if e%2==0] + [e for e in A if e%2==1]

input = list(map(int,read().rstrip().lstrip('[').rstrip(']')))
mod = Solution()
print(mod.sortArrayByParity(input))
