from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(x for x,y in points) # Extract only the x-coordinates because you need to find neighboring x-coordinates that make the biggest difference among x-coordinates.
        maxlen = 0
        for i in range(len(xs)-1): # Find two points that show the biggest difference.
            maxlen = max(maxlen, xs[i+1]-xs[i])
        return maxlen

inputs = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
points = []
for e in inputs:
    points.append(list(map(int,e.split(','))))
mod = Solution()
print(mod.maxWidthOfVerticalArea(points))
