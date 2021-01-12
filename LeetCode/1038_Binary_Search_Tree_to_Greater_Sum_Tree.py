from collections import deque
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
        if self.root == None:
            self.root = node
            return
        cur = self.root
        while True:
            if node.val > cur.val:
                if cur.right == None:
                    cur.right = node
                    return
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                    return
                else:
                    cur = cur.left

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def __init__(self):
        self.sum = 0

    def addNode(self, node):
        # Calculate from the deepest node on the right and gradually move to the lower left node.
        if node.right:
            self.addNode(node.right)
        node.val += self.sum
        self.sum = node.val
        if node.left:
            self.addNode(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.addNode(root)
        return root

# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         def addNode(node):
#             if node.right:
#                 addNode(node.right)
#             node.val += self.sum
#             self.sum = node.val
#             if node.left:
#                 addNode(node.left)
#
#         self.sum = 0
#         addNode(root)
#         return root

values = list(read().rstrip().split(','))
nodes = []
for value in values:
    if value == 'null':
        continue
    nodes.append(TreeNode(int(value)))

binary_tree = BinaryTree()
for node in nodes:
    binary_tree.insertNode(node)
# binary_tree.printNode(binary_tree.root)

mod = Solution()
binary_tree.printNode(mod.bstToGst(binary_tree.root))
