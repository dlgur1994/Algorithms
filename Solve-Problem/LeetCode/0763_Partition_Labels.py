from typing import List
from collections import defaultdict
import sys

read = sys.stdin.readline

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = defaultdict(int)
        id, ptr = -1, 0
        ans = [0]
        for i, s in enumerate(S): # Store the last location of each element.
            last[s] = i
        for i, s in enumerate(S):
            id = max(id, last[s]) # id refers to the backmost position of the elements in a bundle.
            if id == i: # If the elements so far are no longer behind.
                ans.append(i-ptr+1) # Append the length of the bundle to ans.
                ptr += ans[-1] # Move ptr to the next position of the bundle.
        return ans[1:] # The first element of ans is zero, so return the remaining element except it.

S = read().rstrip()
mod = Solution()
print(mod.partitionLabels(S))
