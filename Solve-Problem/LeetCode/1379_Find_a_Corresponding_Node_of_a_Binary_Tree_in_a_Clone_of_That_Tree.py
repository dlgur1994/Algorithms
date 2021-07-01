from collections import deque
import sys

read = sys.stdin.readline

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, cen, left, right):
        if self.root is None:
            self.root = cen
        cen.val = int(cen.val)
        cen.left = left
        cen.right = right

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)]) # Store the original and cloned nodes together.
        while q:
            origin, clon = q.popleft()
            if origin is target: # When the target node is found, returns the cloned node.
                return clon
            if origin.left:
                q.append((origin.left, clon.left))
            if origin.right:
                q.append((origin.right, clon.right))

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         q = deque([cloned])
#         while q:
#             cur = q.popleft()
#             if cur.val == target.val:
#                 return cur
#             if cur.left:
#                 q.append(cur.left)
#             if cur.right:
#                 q.append(cur.right)

values = list(read().rstrip().split(','))
tar_val = int(read().rstrip())
nodes = []
for val in values:
    if val != 'null':
        val = int(val)
    nodes.append(TreeNode(val))
binary_tree1 = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree1.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
for node in nodes:
    if node.val == tar_val:
        target = node
# binary_tree1.printNode(binary_tree1.root)
binary_tree2 = binary_tree1
mod = Solution()
print(mod.getTargetCopy(binary_tree1.root, binary_tree2.root, target))
