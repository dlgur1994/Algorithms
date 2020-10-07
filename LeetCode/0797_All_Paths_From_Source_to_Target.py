from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(start,ends):
            visited = [start]
            stack = ends

            for node in stack:
                if graph[node]==[]:
                    break
                visited.extend(dfs(node,graph[node]))

            return visited

        routes = []
        for i in range(len(graph)):
            if graph[i]==[]:
                continue
            routes.append(dfs(i,graph[i]))
        return routes

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
