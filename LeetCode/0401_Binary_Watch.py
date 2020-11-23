from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]
        output = []

        for i in range(num+1):
            if i==0:
                h = 0
                mi =
            elif i==1:
                h =
                mi =
            output.append((hr,mi))

        return output

input_val = int(read().rstrip())
mod = Solution()
print(mod.readBinaryWatch(input_val))
