from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(start,end):
            route = [start]
            option = [[start] for i in range(len(end))]
            for i in range(len(end)):
                option[i].append(dfs(end[i],graph[end[i]]))
            return option

        output = []
        for i in range(len(graph)):
            output.append(dfs(i,graph[i]))
        return output

input = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
for i in range(len(input)):
    if len(input[i])==0:
        input[i] = []
        continue
    if len(input[i])==1:
        input[i] = list(map(int,input[i]))
        continue
    input[i] = list(map(int,input[i].split(',')))
mod = Solution()
print(mod.allPathsSourceTarget(input))
