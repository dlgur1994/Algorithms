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
        self.new_root = None

    def getNodes(self, node):
        if node.left:
            self.getNodes(node.left)
        self.nodes.append(node)
        if node.right:
            self.getNodes(node.right)

    def makeTree(self, l):
        if self.new_root == None:
            self.new_root = l[len(l)//2]
            self.new_root.left = l[len(l)//4]
            self.new_root.right = l[len(l)//4*3]
        else:
            cur = self.new_root
            while cur:


    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.getNodes(root)
        self.makeTree()
        return self.new_root

vals = list(map(int, read().rstrip().split(',')))
binary_tree = BinaryTree()
for val in vals:
    binary_tree.insertNode(TreeNode(val))
# binary_tree.printNode(binary_tree.root)
mod = Solution()
print(mod.balanceBST(binary_tree.root))
