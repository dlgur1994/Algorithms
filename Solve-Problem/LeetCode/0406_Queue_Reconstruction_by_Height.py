from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [0] * len(people)
        people = sorted(people, key=lambda x:x[0])

        return ans

temp = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
people = []
for e in temp:
    people.append(list(map(int,e.split(','))))
mod = Solution()
print(mod.reconstructQueue(people))
