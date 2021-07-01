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
        cen.val = int(cen.val)
        if self.root == None:
            self.root = cen
        if left.val != 'null':
            left.val = int(left.val)
            cen.left = left
        if right.val != 'null':
            right.val = int(right.val)
            cen.right = right

    def printNode(self, node):
        print(node.val, type(node.val))
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def findSumAndTilt(self, node):
        if not node:
            return 0, 0
        left_sum, left_tilt = self.findSumAndTilt(node.left)
        right_sum, right_tilt = self.findSumAndTilt(node.right)
        return node.val+left_sum+right_sum, left_tilt+right_tilt+abs(left_sum-right_sum)

    def findTilt(self, root: TreeNode) -> int:
        return self.findSumAndTilt(root)[1]

# class Solution:
#     def findTilt(self, root: TreeNode) -> int:
#         def nodeSum(node):
#             sum = node.val
#             if node.left:
#                 sum += nodeSum(node.left)
#             if node.right:
#                 sum += nodeSum(node.right)
#             return sum
#
#         def dfs(node):
#             if node.left and node.right:
#                 self.result += abs(nodeSum(node.left) - nodeSum(node.right))
#                 dfs(node.left)
#                 dfs(node.right)
#             elif node.left:
#                 self.result += abs(nodeSum(node.left))
#                 dfs(node.left)
#             elif node.right:
#                 self.result += abs(nodeSum(node.right))
#                 dfs(node.right)
#
#         self.result = 0
#         if root:
#             dfs(root)
#         return self.result

nodes = list(map(TreeNode,read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)

mod = Solution()
print(mod.findTilt(binary_tree.root))
