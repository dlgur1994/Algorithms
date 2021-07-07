import sys
read = sys.stdin.readline
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1,numRows+1):
            row = [1 for _ in range(i)]
            if i>2:
                for j in range(1,i-1):
                    row[j]=triangle[i-2][j-1]+triangle[i-2][j]
            triangle.append(row)
        return triangle

input_num = int(read().rstrip())
mod = Solution()
print(mod.generate(input_num))
