from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def sumZero(self, n: int) -> List[int]:
        output,k = [],1
        if n%2==1:
            output.append(0)
        for _ in range(0,int(n/2)):
            output.append(k)
            output.append(-k)
            k += 1
        return output

input = int(read().rstrip())
mod = Solution()
print(mod.sumZero(input))
