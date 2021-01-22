from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ids = []
        start, end = 0, 1

        for i in range(len(S)):
            check = end
            for val in S[start:end]:
                if len(S)-1-S[::].index(S[i]) > end:
                    end = S.index(S[i])
                    print('1', end)
            if check == end:
                ids.append(end)
                end += 1
                start = end
        # return ids

S = read().rstrip()
mod = Solution()
print(mod.partitionLabels(S))
