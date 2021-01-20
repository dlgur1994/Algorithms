from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        vals = [S[0]]
        cuts = []
        id = 0

        for i in range(1,len(S)):
            if S[i] not in S[i+1:]:
                for e in vals:
                    if e in S[i+1:]:
                         break
            elif S[i] not in vals:
                vals.append(S[i])

        # while S:
        #     rev = S[::-1]
        #     vals = S[id:len(S)-rev.index(S[id])]
        #     print(vals)
        #     id = len(S)-rev.index(S[id])
        #     for val in vals:
        #         if val in S[id:]:
        #             id = len(S)-rev.index(S[val])
        #     S = S[id:]



S = read().rstrip()
mod = Solution()
print(mod.partitionLabels(S))
