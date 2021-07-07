from typing import List
import heapq
import sys

read = sys.stdin.readline

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,(-stone, stone))
        while len(heap)>1:
            temp = []
            for _ in range(2):
                temp.append(heapq.heappop(heap)[1])
            if temp[0] != temp[1]:
                heapq.heappush(heap,(-(temp[0]-temp[1]), temp[0]-temp[1]))
        return heap[0][1] if len(heap)==1 else 0

input_list = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.lastStoneWeight(input_list))
