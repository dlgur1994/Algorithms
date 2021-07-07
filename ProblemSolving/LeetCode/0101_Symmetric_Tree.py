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

    def insertNode(self, node_cen, node_left, node_right):
        if self.root == None:
            self.root = node_cen
        node_cen.left = node_left
        node_cen.right = node_right

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checkSymmetric(left, right):
            # it's a leaf, so it's symmetrical
            if not left and not right:
                return True

            # having only one left or right means asymmetric
            elif not left or not right:
                return False

            # repeat if left and right values are equal
            elif left.val == right.val:
                return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)

            else:
                return False

        # if root empty, just return False
        if not root:
            return False
        return checkSymmetric(root.left, root.right)

nodes = list(map(TreeNode, read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)

mod = Solution()
print(mod.isSymmetric(binary_tree.root))
