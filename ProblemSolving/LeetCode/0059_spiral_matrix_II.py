import sys
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        x, y = 0, 0
        num, cnt = 1, n
        while num < n*n+1:
            for _ in range(0, cnt):
                matrix[y][x] = num
                num += 1
                x += 1
            x -= 1
            y += 1
            cnt -= 1
        
            for _ in range(0, cnt):
                matrix[y][x] = num
                num += 1
                y += 1
            x -= 1
            y -= 1

            for _ in range(0, cnt):
                matrix[y][x] = num
                num += 1
                x -= 1
            x += 1
            y -= 1
            cnt -= 1
           
            for _ in range(0, cnt):
                matrix[y][x] = num
                num += 1
                y -= 1
            x += 1
            y += 1

        return matrix

n = int(sys.stdin.readline().rstrip())
mod = Solution()
print(mod.generateMatrix(n))