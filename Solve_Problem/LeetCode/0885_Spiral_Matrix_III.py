from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        output = ([[r0,c0]])
        cnt = 0
        while len(output)< R*C: # Verify that all elements are in output
            for j in range(2*cnt+1): # go 2n+1 times to the right
                c0 += 1
                if r0>-1 and r0<R and c0>-1 and c0<C: # Check the coordinate is in range
                    output.append([r0, c0])
            for j in range(2*cnt+1): # go down 2n+1 times
                r0 += 1
                if r0>-1 and r0<R and c0>-1 and c0<C:
                    output.append([r0, c0])
            for j in range(2*cnt+2): # go 2n+1 times to the left
                c0 -= 1
                if r0>-1 and r0<R and c0>-1 and c0<C:
                    output.append([r0, c0])
            for j in range(2*cnt+2): # go up 2n+1 times
                r0 -= 1
                if r0>-1 and r0<R and c0>-1 and c0<C:
                    output.append([r0, c0])
            cnt += 1
        return output

R, C, r0, c0 = map(int, read().rstrip().split(','))
mod = Solution()
print(mod.spiralMatrixIII(R,C,r0,c0))
