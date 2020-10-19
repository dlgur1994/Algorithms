from typing import List
from collections import deque
import sys
read = sys.stdin.readline

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited = []
        deque = ([])
        max_time = 0
        for i in range(len(times)):
            if times[i][0]==K:
                deque.append(times[i])

        while deque:
            source,target,time = deque.pop(0)
            if target not in visited:
                visited.append((K,target,time))
            for e in times:

            # if time>max_time: max_time=time
            # for i in range(len(times)):
            #     if times[i][0]==target:
            #         times[i][2]+=time
            #         deque.append(times[i])
            # if target not in visited:
            #     visited.append(target)
            # if len(visited)==N:
            #     return max_time

        return -1

input_list = read().rstrip().lstrip('[[').rstrip(']]').split('],[')
refined_input_list = [[int(e) for e in element.split(',')] for element in input_list]
node_num,source = map(int,read().rstrip().split(','))
mod = Solution()
print(mod.networkDelayTime(refined_input_list,node_num,source))

'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited = [K]
        deque = ([])
        max_time = 0
        for i in range(len(times)):
            if times[i][0]==K:
                deque.append(times[i])

        while deque:
            source,target,time = deque.pop(0)
            if time>max_time: max_time=time
            for i in range(len(times)):
                if times[i][0]==target:
                    times[i][2]+=time
                    deque.append(times[i])
            if target not in visited:
                visited.append(target)
            if len(visited)==N:
                return max_time

        return -1
'''
