import sys
from typing import List

read = sys.stdin.readline

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda p:p[0]*p[0]+p[1]*p[1]) # sort by the distance
        return points[:k]

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         length = dict()
#         cnt = 0
#         ans = []
#         for point in points:
#             length[cnt] = point[0]*point[0] + point[1]*point[1]
#             cnt += 1
#         length = sorted(length.items(), key=lambda item:item[1])
#         for i in range(k):
#             ans.append(points[length[i][0]])
#         return ans

points = []
temp = read().rstrip().lstrip('[').rstrip(']').split('],[')
k = int(read().rstrip())
for e in temp:
    points.append(list(map(int,e.split(','))))
mod = Solution()
print(mod.kClosest(points, k))
