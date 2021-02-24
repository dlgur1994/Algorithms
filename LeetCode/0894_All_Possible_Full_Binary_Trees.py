import sys

read = sys.stdin.readline


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, node):


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2 == 0:
            return None
        else:
            

N = int(read().rstrip())
mod = Solution()
print(mod.allPossibleFBT(N))
