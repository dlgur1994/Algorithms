from collections import deque
import sys
read = sys.stdin.readline

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t) # This prevents the queue from being empty
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)

# class RecentCounter:
#     def __init__(self):
#         self.cnt = 0
#         self.queue = []
#
#     def ping(self, t: int) -> int:
#         check = -1
#         for i in range(len(self.queue)):
#             if self.queue[i] < t-3000:
#                 check = i
#         self.queue = self.queue[check+1:]
#         self.queue.append(t)
#         print(self.queue)

pings = list(map(int, read().rstrip().split(',')))
obj = RecentCounter()
cnt_list = []
for ping in pings:
    cnt_list.append(obj.ping(ping))
print(cnt_list)
