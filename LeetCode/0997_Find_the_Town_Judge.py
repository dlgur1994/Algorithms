from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        

N = int(read().rstrip())
temp = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
trust = []
for e in temp:
    trust.append(list(map(int,e.split(','))))

mod = Solution()
print(mod.findJudge(N, trust))
