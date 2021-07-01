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
        if node_left.val != 'null':
            node_cen.left = node_left
        if node_right.val != 'null':
            node_cen.right = node_right

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        # if only one node has a child or children
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # keep compare the left and right side of each node
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         stack1 = [p]
#         stack2 = [q]
#         while stack1:
#             node1 = stack1.pop()
#             node2 = stack2.pop()
#             if node1.val != node2.val:
#                 return False
#             if node1.right:
#                 stack1.append(node1.right)
#             if node2.right:
#                 stack2.append(node2.right)
#             if len(stack1) != len(stack2):
#                 return False
#             if node1.left:
#                 stack1.append(node1.left)
#             if node2.left:
#                 stack2.append(node2.left)
#             if len(stack1) != len(stack2):
#                 return False
#         return True

nodes1 = list(map(TreeNode, read().rstrip().split(',')))
nodes2 = list(map(TreeNode, read().rstrip().split(',')))
binary_tree1 = BinaryTree()
binary_tree2 = BinaryTree()
for i in range(len(nodes1)//2):
    binary_tree1.insertNode(nodes1[i], nodes1[2*i+1], nodes1[2*i+2])
for i in range(len(nodes2)//2):
    binary_tree2.insertNode(nodes2[i], nodes2[2*i+1], nodes2[2*i+2])
# binary_tree1.printNode(binary_tree1.root)
# binary_tree2.printNode(binary_tree2.root)

mod = Solution()
print(mod.isSameTree(binary_tree1.root, binary_tree2.root))
