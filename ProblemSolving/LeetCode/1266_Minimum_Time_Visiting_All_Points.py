from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        Diagonal movement allows coordinates to be moved with minimal movement.
        Therefore, I obtain the maximum number of diagonal movements between two points.
        This is the smaller of the x-coordinates or the y-coordinates.
        Then add a move that cannot be made diagonally.
        '''
        cnt = 0
        for i in range(len(points)-1):
            x = abs(points[i][0]-points[i+1][0])
            y = abs(points[i][1]-points[i+1][1])
            min_val = min(x,y)
            cnt += x+y-min_val
        return cnt

inputs = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
points = []
for e in inputs:
    points.append(list(map(int,e.split(','))))
mod = Solution()
print(mod.minTimeToVisitAllPoints(points))
