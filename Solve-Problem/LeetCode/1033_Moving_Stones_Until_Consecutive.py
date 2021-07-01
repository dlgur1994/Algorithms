from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        min = 2
        if b==a+1 or b==a+2 or c==b+1 or c==b+2: # Either two of a,b,c are side by side or two of a,b,c are two spaces apart.
            min = 1
        if b==a+1 and c==b+1: # when a,b and c are next to each other
            min = 0
        lmax = (b-a-1) if b>a+1 else 0 # Number of all cases that can come from the left
        rmax = (c-b-1) if c>b+1 else 0 # Number of all cases that can come from the right
        return min, lmax+rmax

a,b,c = map(int, read().rstrip().split(','))
mod = Solution()
print(mod.numMovesStones(a,b,c))
