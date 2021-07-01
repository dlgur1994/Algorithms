from typing import List
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

    def insertNode(self, cen, left, right):
        if self.root == None:
            cen.val = int(cen.val)
            self.root = cen
        if left.val != "null":
            left.val = int(left.val)
            cen.left = left
        if right.val != "null":
            right.val = int(right.val)
            cen.right = right

    def printNode(self, node):
        if node.left:
            self.printNode(node.left)
        print(node.val)
        if node.right:
            self.printNode(node.right)

class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        if root.left:
            self.inorderTraversal(root.left)
        self.ans.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.ans

nodes = list(map(TreeNode, read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)
mod = Solution()
print(mod.inorderTraversal(binary_tree.root))
