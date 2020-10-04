import sys
read = sys.stdin.readline

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insertNode(self,node,left_node,right_node):
        if self.root is None:
            self.root = node
        if left_node is not None and left_node.val != 'null':
            node.left = left_node
        if right_node is not None and right_node.val != 'null':
            node.right = right_node
    def preOrder(self,node):
        if node == None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getDepth(node):
            if node is None:
                return 0
            left_depth = getDepth(node.left)
            right_depth = getDepth(node.right)
            return left_depth+1 if left_depth>right_depth else right_depth+1

        return getDepth(root)

binary_tree = BinaryTree()
input = list(map(TreeNode,read().rstrip().lstrip('[').rstrip(']').split(',')))
if len(input) == 1:
    input.append(None)
    input.append(None)
if len(input) == 2:
    input.append(None)
for i in range(len(input)//2):
     binary_tree.insertNode(input[i],input[2*i+1],input[2*i+2])
binary_tree.preOrder(binary_tree.root)
mod = Solution()
print(mod.maxDepth(binary_tree.root))
