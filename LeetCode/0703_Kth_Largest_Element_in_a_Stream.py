from typing import List
import heapq
import sys

read = sys.stdin.readline

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums, reverse=True)
        nums = nums[:k]
        heapq.heapify(nums)
        self.heap = heapq.nlargest(k, nums)
        self.k = k

    def add(self, val: int) -> int:
        if self.heap == []:
            self.heap.append(val)
            return val
        if val > self.heap[-1]:
            heapq.heapify(self.heap)
            heapq.heappush(self.heap, val)
            self.heap = heapq.nlargest(self.k, self.heap)
        return self.heap[-1]

# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         heapq.heapify(nums)
#         self.heap = heapq.nlargest(k, nums)
#         self.k = k
#
#     def add(self, val: int) -> int:
#         if self.heap == []:
#             self.heap.append(val)
#             return val
#         if val > self.heap[-1]:
#             heapq.heapify(self.heap)
#             heapq.heappush(self.heap, val)
#             self.heap = heapq.nlargest(self.k, self.heap)
#         return self.heap[-1]

input_val = int(read().rstrip())
input_list = list(map(int,read().rstrip().split(',')))
obj = KthLargest(input_val, input_list)
param_1 = obj.add(3)
param_2 = obj.add(5)
param_3 = obj.add(10)
param_4 = obj.add(9)
param_5 = obj.add(4)
print(param_1, param_2, param_3, param_4, param_5)
