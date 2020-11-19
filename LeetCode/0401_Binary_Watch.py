from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]
        output = []

        for i in range(num):
            hr = 0
            mi = 0
            output.append((hr,mi))

        return output

input_val = int(read().rstrip())
mod = Solution()
print(mod.readBinaryWatch(input_val))
