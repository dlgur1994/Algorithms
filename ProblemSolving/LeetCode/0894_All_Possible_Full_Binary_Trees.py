from typing import List
import sys

read = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1: # If N is 1, only one case is possible
            return [TreeNode(0)]
        elif N%2 == 0: # When N is a multiple of 2, the number of children cannot be zero or two
            return []
        else:
            ans = []
            l = N-2 # When the root and right nodes were subtracted from the tree of three nodes
            r = 1 # the right node
            while l > 0:
                left = self.allPossibleFBT(l) # Save every possible case on the left
                right = self.allPossibleFBT(r) # Save every possible case on the right
                for i in range(len(left)):
                    for j in range(len(right)):
                        root = TreeNode(0)
                        root.left = left[i]
                        root.right = right[j]
                        ans.append(root)
                l -= 2
                r += 2
            return ans

def printNode(node):
    print(node.val)
    if not node.left:
        print("null")
    if node.left:
        printNode(node.left)
    if not node.right:
        print("null")
    if node.right:
        printNode(node.right)

N = int(read().rstrip())
mod = Solution()
roots = mod.allPossibleFBT(N)
for root in roots:
    printNode(root)
    print('""')
