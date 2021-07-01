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
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def __init__(self):
        self.nodes = []

    def getNodes(self, node): # create a list of nodes in ascending order of node values.
        if node.left:
            self.getNodes(node.left)
        self.nodes.append(node)
        if node.right:
            self.getNodes(node.right)

    def makeTree(self, start, end): # create a binary search tree
        if start >= end:
            return None
        mid = (start+end)//2
        mid_node = self.nodes[mid]
        mid_node.left = self.makeTree(start, mid)
        mid_node.right = self.makeTree(mid+1, end)
        return mid_node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.getNodes(root)
        return self.makeTree(0, len(self.nodes))

vals = list(read().rstrip().split(','))
binary_tree = BinaryTree()
for val in vals:
    binary_tree.insertNode(TreeNode(val))
# binary_tree.printNode(binary_tree.root)
mod = Solution()
print(mod.balanceBST(binary_tree.root))
