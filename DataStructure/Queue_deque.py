from collections import deque

queue = deque()
queue.append(3)
queue.append(4)
queue.append(5)

queue.popleft()
print(queue)

queue.pop()
print(queue)

queue.appendleft(6)
print(queue)
