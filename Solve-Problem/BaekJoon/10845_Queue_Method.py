import sys

class Queue():
    def __init__(self):
        self.lst = []

    def push(self,data):
        self.lst.append(data)

    def pop(self):
        if(self.empty() == 1):
            return -1
        else:
            num = self.lst[0]
            del self.lst[0]
            return num

    def size(self):
        return len(self.lst)

    def empty(self):
        if(self.size()==0):
            return 1
        else:
            return 0

    def front(self):
        if(self.empty() == 1):
            return -1
        return self.lst[0]

    def back(self):
        if(self.empty() == 1):
            return -1
        return self.lst[self.size()-1]

q = Queue()
numOfCom = int(sys.stdin.readline())
for i in range(numOfCom):
    strCom = sys.stdin.readline().split()
    if(strCom[0] == 'push'):
        q.push(strCom[1])
    elif(strCom[0] == 'pop'):
        print(q.pop())
    elif(strCom[0] == 'size'):
        print(q.size())
    elif(strCom[0] == 'empty'):
        print(q.empty())
    elif(strCom[0] == 'front'):
        print(q.front())
    elif(strCom[0] == 'back'):
        print(q.back())
    else:
        print('Error')
