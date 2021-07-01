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

    def insertNode(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            while cur:
                if node.val > cur.val:
                    if not cur.right:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                else:
                    if not cur.left:
                        cur.left = node
                        break
                    else:
                        cur = cur.left

    def printNode(self, node):
        if node.left:
            self.printNode(node.left)
        print(node.val)
        if node.right:
            self.printNode(node.right)

class Solution:
    def __init__(self):
        self.buf = [] # it is a buffer to store values from trees

    def getVals(self, node): # store values in ascending order 
        if node.left:
            self.getVals(node.left)
        self.buf.append(node.val)
        if node.right:
            self.getVals(node.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if root1: # get every value in the first tree
            self.getVals(root1)
        if root2: # get every value in the second tree
            self.getVals(root2)
        return sorted(self.buf)

vals1 = list(map(int, read().rstrip().split(',')))
vals2 = list(map(int, read().rstrip().split(',')))
binary_tree1 = BinaryTree()
binary_tree2 = BinaryTree()
for val in vals1:
    binary_tree1.insertNode(TreeNode(val))
for val in vals2:
    binary_tree2.insertNode(TreeNode(val))
binary_tree1.printNode(binary_tree1.root)
binary_tree2.printNode(binary_tree2.root)
mod = Solution()
print(mod.getAllElements(binary_tree1.root, binary_tree2.root))
