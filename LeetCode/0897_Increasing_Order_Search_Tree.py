import sys
read = sys.stdin.readline

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,value):
        self.root = TreeNode(value,none,none)


    def insert_node(self,value):

# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:

input = list(read().rstrip(']').lstrip('[').split(','))
tree_node = Tree()
for e in input:
    tree_node.insert_node(e)
# mod = Solution()
# print(mod.increasingBST(input))
