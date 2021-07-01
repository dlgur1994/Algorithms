import sys

class Stack:
    def __init__(self):
        self.lst = []
    def push(self,data):
        self.lst.append(data)
    def pop(self):
        if(not self.empty()):
            return self.lst.pop()
    def empty(self):
        if(len(self.lst)==0):
            return True
        else:
            return False
    def clear(self):
        self.lst = []

s = Stack()
lst = []

while(True):
    strInput = sys.stdin.readline()
    if(strInput == '.\n'):
        break
    else:
        for i in range(len(strInput)-1):
            if (strInput[i] == '(' or strInput[i] == '['):
                s.push(strInput[i])
            elif (strInput[i] == ')'):
                if(s.pop() != '('):
                    s.push('x')
            elif (strInput[i] == ']'):
                if(s.pop() != '['):
                    s.push('x')
    if(s.empty()):
        print('yes')
    else:
        print('no')
    s.clear()
