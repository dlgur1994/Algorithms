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
        if not self.root:
            cen.val = int(cen.val)
            self.root = cen
        if left.val != "null":
            left.val = int(left.val)
            cen.left = left
        if right.val != "null":
            right.val = int(right.val)
            cen.right = right

    def printNode(self, node):
        print(node.val)
        print(type(node.val))
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = {'0' : 0} # The dictionary to store the values of the modified tree.
        root.val = 0
        self.editNode(root) # Modify the values of the tree.

    def find(self, target: int) -> bool:
        if str(target) in self.values: # Check whether the dictionary has a value or not.
            return True
        else:
            return False

    def editNode(self, node):
        if node.left: # If the node has left, modify the value of the left node and save it in the dictionary.
            node.left.val = 2*node.val + 1
            self.values[str(node.left.val)] = 0
            self.editNode(node.left)
        if node.right: # If the node has right, modify the value of the right node and save it in the dictionary.
            node.right.val = 2*node.val + 2
            self.values[str(node.right.val)] = 0
            self.editNode(node.right)

# class FindElements:
#     def __init__(self, root: TreeNode):
#         root.val = 0
#         self.values = [0]
#         self.editNode(root)
#
#     def find(self, target: int) -> bool:
#         if target in self.values:
#             return True
#         else:
#             return False
#
#     def editNode(self, node):
#         if node.left:
#             node.left.val = 2*node.val + 1
#             self.values.append(node.left.val)
#             self.editNode(node.left)
#         if node.right:
#             node.right.val = 2*node.val + 2
#             self.values.append(node.right.val)
#             self.editNode(node.right)

    # def printNode(self, node):
    #     print(node.val)
    #     if node.left:
    #         self.printNode(node.left)
    #     if node.right:
    #         self.printNode(node.right)

nodes = list(map(TreeNode, read().rstrip().split(',')))
targets = list(map(int, read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)

obj = FindElements(binary_tree.root)
# obj.printNode(binary_tree.root)
for target in targets:
    print(obj.find(target))
