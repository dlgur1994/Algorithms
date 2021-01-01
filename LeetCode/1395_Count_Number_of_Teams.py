from typing import List
import sys

read = sys.stdin.readline

'''
Check one by one from the back of the list.
Think of the case in which the number in front (ith) < the number in the back (jth) or 'ith' >= 'jth'.
If 'ith' is greater than 'jth', add 1 to list up[i].
Otherwise, add 1 to list down[i].
Add the number up/down [j] to 'result'.
This is to find something like this situation in the back when it is ith<jth or ith>=jth.
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        up = [0] * n
        down = [0] * n
        result = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    up[i] += 1
                    result += up[j]
                else:
                    down[i] += 1
                    result += down[j]
        return result

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
