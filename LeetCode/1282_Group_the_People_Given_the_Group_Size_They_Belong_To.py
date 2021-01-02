from typing import List
from collections import defaultdict
import sys

read = sys.stdin.readline

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Store the group size of each element in the dictionary.
        check = defaultdict(list)
        for i,e in enumerate(groupSizes):
            check[e].append(i)

        # If the value of the check is greater than the key, divide it and extend it to the result. If not, extend it to the result.
        result = []
        for e in check:
            if len(check[e]) > e:
                for i in range(0,len(check[e]),e):
                    result.append(check[e][i:i+e])
            else:
                result.append(check[e])
        return result

# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         check = {}
#         result = []
#         for i,e in enumerate(groupSizes):
#             if e not in check:
#                 check[e] = [i]
#             else:
#                 check[e].append(i)
#         for e in check:
#             if len(check[e]) > e:
#                 result.extend([check[e][i:i+e] for i in range(0,len(check[e]),e)])
#             else:
#                 result.append(check[e])
#         return result

groupSizes = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.groupThePeople(groupSizes))
