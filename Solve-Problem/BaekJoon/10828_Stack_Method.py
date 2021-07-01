class Stack():
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
            return 1
        else:
            return 0

    def top(self):
        if(self.empty()):
            return -1
        else:
            return self.stack[-1]

import sys

numOfCom = int(sys.stdin.readline())
s = Stack()
for x in range(numOfCom):
    strInput = sys.stdin.readline().split()
    if(strInput[0] == "push"):
        s.push(strInput[1])
    elif(strInput[0] == "pop"):
        print(s.pop())
    elif(strInput[0] == "size"):
        print(s.size())
    elif(strInput[0] == "empty"):
        print(s.empty())
    elif(strInput[0] == "top"):
        print(s.top())
    else:
        print("Error")
