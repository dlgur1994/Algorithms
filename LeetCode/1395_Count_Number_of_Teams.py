from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        up = [0] * n
        down = [0] * n
        teams = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                print(rating[i],rating[j])
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                    print("up",up)
                else:
                    down[i] += 1
                    teams += down[j]
                    print("down", down)
        print(up)
        print(down)
        return teams

# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         cnt = 0
#         for i in range(len(rating)-2):
#             for j in range(i+1,len(rating)-1):
#                 for k in range(j+1, len(rating)):
#                     if rating[i]<rating[j] and rating[j]<rating[k] or rating[i]>rating[j] and rating[j]>rating[k]:
#                         cnt += 1
#         return cnt

rating = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.numTeams(rating))
