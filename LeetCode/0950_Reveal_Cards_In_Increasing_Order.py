from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        output = [-1] * len(deck)
        sort_deck = sorted(deck)
        if len(deck)%2 == 1:
            length1 = len(deck)//2 + 1
        else:
            length1 = len(deck)//2
        length2 = len(deck)-length1
        for i in range(length1):
            output[2*i] = sort_deck[i]
        for i in range(length2):
            output[2*i+1] = sort_deck[length1+i]
        return output

deck = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.deckRevealedIncreasing(deck))
