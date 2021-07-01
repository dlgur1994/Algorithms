from typing import List
import heapq
import sys

read = sys.stdin.readline

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #changed nums to the heap with largest k numbers
        heapq.heapify(nums)
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        #if the length of the heap is smaller less than k, push val into the heap
        if len(self.heap)<self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        #if val is bigger than the smallest number of the heap, pop the heap and push val into the heap
        if val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

input_val = int(read().rstrip())
input_list = list(map(int,read().rstrip().split(',')))
obj = KthLargest(input_val, input_list)
param_1 = obj.add(3)
param_2 = obj.add(5)
param_3 = obj.add(10)
param_4 = obj.add(9)
param_5 = obj.add(4)
print(param_1, param_2, param_3, param_4, param_5)
