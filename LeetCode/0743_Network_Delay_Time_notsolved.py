from typing import List
from collections import deque
import sys
read = sys.stdin.readline

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visited = []
        taken_time = [0 for e in range(N)]
        deque = ([])
        for e in times:
            if e[0]==K:
                deque.append(e)
        while deque:
            source,target,time = deque.pop(0)
            if target in visited:
                if time<taken_time[target-1]:
                    taken_time[target-1] = time
                continue
            visited.append(target)
            taken_time[target-1] = time
            for e in times:
                if e[0]==target:
                    deque.append((e[0],e[1],e[2]+time))
        if taken_time.count(0)>1:
            return -1
        return max(taken_time)

input_list = read().rstrip().lstrip('[[').rstrip(']]').split('],[')
refined_input_list = [[int(e) for e in element.split(',')] for element in input_list]
node_num,source = map(int,read().rstrip().split(','))
mod = Solution()
print(mod.networkDelayTime(refined_input_list,node_num,source))
