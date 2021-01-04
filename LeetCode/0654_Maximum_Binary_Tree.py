from typing import List
import sys

read = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insertNode(self, node):

class Solution:
    def makeNodes(self, l):
        big = max(l)
        left = l[:l.index(big)]
        right = l[l.index(big)+1:]
        return left,right

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        print(self.makeNodes(nums))

nums = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.constructMaximumBinaryTree(nums))
