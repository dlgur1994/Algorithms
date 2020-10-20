import sys
read = sys.stdin.readline
from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        num_squares = []
        for e in A:
            num_squares.append(e*e)
        return sorted(num_squares)
        # return sorted(list(map(lambda x: x*x, A)))

num_list = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.sortedSquares(num_list))
