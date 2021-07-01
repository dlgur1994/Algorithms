class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.min_value = None

    def push(self, x: int) -> None:
        if self.min_value==None or self.min_value>=x:
            self.min_value = x
            self.mins.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.mins[-1]:
            self.mins.pop()
            self.min_value = self.mins[-1] if self.mins != [] else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value

obj = MinStack()
obj.push(1)
obj.push(1)
obj.push(2)
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.mins)
# obj.push(2)
# print(obj.getMin())
# obj.push(-3)
# print(obj.getMin())

# param_3 = obj.top()
# print(param_1)
# param_4 = obj.getMin()
# print(param_1, param_4)
