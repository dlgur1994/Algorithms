class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            return self.stack.pop()
    def peek(self):
        print(self.stack[-1])
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.peek()
print(stack.pop())
stack.peek()
print(stack.pop())
stack.peek()
print(stack.pop())
stack.pop()
