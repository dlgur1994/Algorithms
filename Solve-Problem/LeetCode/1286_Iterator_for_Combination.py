import sys
from itertools import combinations

read = sys.stdin.readline

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.l = list(combinations(characters, combinationLength))
        self.ptr = 0
        for i in range(len(self.l)): # If a list is made with the combination function, each element must be replaced with a word because each element consists of letters connected by ',' rather than words.
            self.l[i] = ''.join(self.l[i])

    def next(self) -> str:
        self.ptr += 1
        return self.l[self.ptr-1]

    def hasNext(self) -> bool:
        return True if self.ptr<len(self.l) else False

characters = read().rstrip()
combinationLength = int(read().rstrip())
obj = CombinationIterator(characters, combinationLength)
param_1 = obj.next()
param_2 = obj.hasNext()
print(param_1, param_2)
