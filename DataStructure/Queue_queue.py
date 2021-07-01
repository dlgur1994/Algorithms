from queue import Queue

queue = Queue()
queue.put(3)
queue.put(4)
queue.put(5)
queue

print(queue.get())
print(queue.get())
