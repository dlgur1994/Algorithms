from typing import List
from collections import deque
import sys

read = sys.stdin.readline

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        id = deque(range(len(deck)))
        output = [-1] * len(deck)

        # It is a way of simulating the conditions of the problem as they are.
        for e in sorted(deck):
            output[id.popleft()] = e
            if id: # If the list id is present, send the first element to the back.
                id.append(id.popleft())
        return output

deck = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.deckRevealedIncreasing(deck))
