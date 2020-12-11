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
    def minDepth(self, root: TreeNode) -> int:
        # when root is null
        if not root:
            return 0
        depth = 1
        queue = deque([(root, depth)])
        while queue:
            node, dep = queue.popleft()

            # when a node is a leaf node
            if not node.left and not node.right:
                return dep
            if node.left:
                queue.append((node.left, dep+1))
            if node.right:
                queue.append((node.right, dep+1))

nodes = list(map(TreeNode, read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)

mod = Solution()
print(mod.minDepth(binary_tree.root))
