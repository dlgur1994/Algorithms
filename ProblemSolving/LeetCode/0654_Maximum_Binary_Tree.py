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
        if not l:
            return None
        else:
            node = TreeNode(max(l)) # find the largest number and make it a treenode
            id = l.index(max(l)) # find the index of the biggest number
            node.left = self.makeNodes(l[:id]) # the node's left
            node.right = self.makeNodes(l[id+1:]) # the node's right
            return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = self.makeNodes(nums)
        return root

def printNodes(node):
    print(node.val)
    if node.left:
        printNodes(node.left)
    if node.right:
        printNodes(node.right)

nums = list(map(int, read().rstrip().split(',')))
mod = Solution()
printNodes(mod.constructMaximumBinaryTree(nums))
