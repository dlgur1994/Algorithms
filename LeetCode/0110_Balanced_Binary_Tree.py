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
            self.root = cen
        if left.val != 'null':
            cen.left = left
        if right.val != 'null':
            cen.right = right

    def printNodes(self, node):
        print(node.val)
        if node.left:
            self.printNodes(node.left)
        if node.right:
            self.printNodes(node.right)

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left) # Depth on the left
        right = self.dfs(node.right) # Depth on the right
        if abs(left-right) > 1: # If the difference between the depth on the left and the depth on the right is greater than 1, then the condition is not high-balance binary tree.
            raise Exception()
        return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        try:
            self.dfs(root)
        except:
            return False
        return True

nodes = list(map(TreeNode, read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNodes(binary_tree.root)

mod = Solution()
print(mod.isBalanced(binary_tree.root))
