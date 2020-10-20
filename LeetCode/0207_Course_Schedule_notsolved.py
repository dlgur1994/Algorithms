import sys
read = sys.stdin.readline
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites==[]:
            return True
        permitted = []
        deque = ([(prerequisites[0])])
        del(prerequisites[0])
        print(prerequisites)
        # while deque:
        #     prev,next = deque.popleft()
        #     if (prev,next) not in permitted:
        #         permitted.append((prev,next))
        #         for e in prerequisites:
        #
        # return visited

num_of_course = int(read().rstrip())
relat_list = list(read().rstrip().lstrip('[[').rstrip(']]').split('],['))
relat_list = [[int(a) for a in e.split(',')] for e in relat_list]
mod = Solution()
print(mod.canFinish(num_of_course,relat_list))
#[[1,0],[0,1]]
