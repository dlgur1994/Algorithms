class MyQueue:
    def __init__(self):
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        self.stackout = self.stackin[::-1]
        self.stackin = self.stackin[1::]
        return self.stackout.pop()

    def peek(self) -> int:
        return self.stackin[0]

    def empty(self) -> bool:
        return True if len(self.stackin)==0 else False

obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)
