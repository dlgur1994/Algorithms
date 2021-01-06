from typing import List
import sys

read = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def makeNodes(self, l):
        if l == None:
            return None
        else:
            node = TreeNode(max(l))
            id = l.index(max(l))
            node.left = self.makeNodes(l[:id])
            node.right = self.makeNodes(l[id+1:])
        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = self.makeNodes(nums)
        return root

nums = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.constructMaximumBinaryTree(nums))
