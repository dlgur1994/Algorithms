class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,push_data):
        new_node = Node(push_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            pop_data = self.head.data
            self.head = self.head.next
            return pop_data

    def peek(self):
        print(self.head.data)

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)

stack.peek()
print(stack.pop())
stack.peek()
print(stack.pop())
stack.peek()
print(stack.pop())
