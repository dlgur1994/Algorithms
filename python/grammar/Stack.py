class Stack(list):
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if(self.empty()):
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False

    def top(self):
        if(self.empty()):
            return -1
        else:
            return self.stack[-1]

if __name__ == "__main__":
    s= Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.pop())
    print(s.top())
    print(s.pop())
    print(s.pop())
    print(s.pop())
