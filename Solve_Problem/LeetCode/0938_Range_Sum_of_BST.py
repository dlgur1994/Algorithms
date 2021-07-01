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
        self.cur = self.root
        if self.root == None:
            self.root = node
            return
        else:
            while True:
                if self.cur.val > node.val:
                    if self.cur.left == None:
                        self.cur.left = node
                        return
                    else:
                        self.cur = self.cur.left
                else:
                    if self.cur.right == None:
                        self.cur.right = node
                        return
                    else:
                        self.cur = self.cur.right

    def printNode(self,node):
        if node == None:
            return
        print(node.val)
        self.printNode(node.left)
        self.printNode(node.right)

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def getNode(node):
            # this is a break condition
            if node == None:
                return

            # when the value is in the range
            elif node.val >= low and node.val <= high:
                vals.append(node.val)
                getNode(node.left)
                getNode(node.right)

            # if the value is less than low, the right node of the node should be checked
            elif node.val < low:
                getNode(node.right)

            # if the value is greater than high, the left node of the node should be checked
            elif node.val > high:
                getNode(node.left)
                
        vals = []
        getNode(root)
        return sum(vals)

vals = list(map(int, read().split(',')))
low, high = map(int, read().split(','))

binary_tree = BinaryTree()
for e in vals:
    binary_tree.insertNode(TreeNode(e))
# binary_tree.printNode(binary_tree.root)

mod = Solution()
print(mod.rangeSumBST(binary_tree.root, low, high))
