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
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = node
                        break
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = node
                        break

    def printNode(self, node):
        if node.left:
            self.printNode(node.left)
        print(node.val)
        if node.right:
            self.printNode(node.right)

class Solution:
    def __init__(self):
        self.ans = 0
        self.cnt = 0
        self.flag = True

    def inOrder(self, node, k):
        if self.flag: # it's an inorder traversal
            if node.left:
                self.inOrder(node.left, k)
            self.cnt += 1
            if self.cnt == k: # it's the stopping point
                self.ans = node.val
                self.flag = False
            if node.right:
                self.inOrder(node.right, k)
        else:
            return self.ans

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inOrder(root, k)
        return self.ans

# class Solution:
#     def __init__(self):
#         self.vals = []
#
#     def inOrder(self, node):
#         if node.left:
#             self.inOrder(node.left)
#         self.vals.append(node.val)
#         if node.right:
#             self.inOrder(node.right)
#
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         self.inOrder(root)
#         return self.vals[k-1]

vals = list(map(int, read().rstrip().split(',')))
binary_tree = BinaryTree()
for val in vals:
    binary_tree.insertNode(TreeNode(int(val)))
k = int(read().rstrip())
# binary_tree.printNode(binary_tree.root)
mod = Solution()
print(mod.kthSmallest(binary_tree.root, k))
