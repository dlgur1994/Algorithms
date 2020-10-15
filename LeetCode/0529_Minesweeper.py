import sys
read = sys.stdin.readline

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def bfs(row,col):
            visited = []
            queue = deque([(row,col)])
            while queue:
                r,c = queue.popleft()
                if node not in visited:
                    visited.append(node)
                queue.append(node)

        while True:
            row,col = read().rstrip.lstrip('[').rstrip(']').split(',')


input = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
input_refined = []
for e in input:
    input_refined.append(list(e.split(',')))
mod = Solution()
print(mod.updateBoard(input_refined))
# [[E,E,E,E,E],[E,E,M,E,E],[E,E,E,E,E],[E,E,E,E,E]]
