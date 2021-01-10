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
        que = deque([(original, cloned)])
        while que:
            orgin, clon = que.popleft()
            if orgin is target:
                return clon
            if orgin.left:
                que.append((orgin.left, clon.left))
            if orgin.right:
                que.append((orgin.right, clon.left))

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         self.q = deque([cloned])
#         while self.q:
#             cur = self.q.popleft()
#             if cur.val == target:
#                 return cur
#             if cur.left:
#                 self.q.append(cur.left)
#             if cur.right:
#                 self.q.append(cur.right)

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
