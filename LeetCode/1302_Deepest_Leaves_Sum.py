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
        if self.root == None:
            self.root = cen
        cen.val = int(cen.val)
        if left.val != 'null':
            left.val = int(left.val)
            cen.left = left
        if right.val != 'null':
            right.val = int(right.val)
            cen.right = right

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, cnt):
            # store the depth and value of a leaf node
            if not node.left and not node.right:
                self.deep.append(cnt)
                self.values.append(node.val)
            if node.left:
                dfs(node.left, cnt+1)
            if node.right:
                dfs(node.right, cnt+1)

        self.deep, self.values = [], []
        sum = 0
        dfs(root, 0)

        # Find the depth of the deepest and add values of the deepest nodes.
        maxdep = max(self.deep)
        for i in range(len(self.deep)):
            if self.deep[i] == maxdep:
                sum += self.values[i]
        return sum

nodes = list(map(TreeNode,read().rstrip().split(',')))
binary_tree = BinaryTree()
for i in range(len(nodes)//2):
    binary_tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# binary_tree.printNode(binary_tree.root)
mod = Solution()
print(mod.deepestLeavesSum(binary_tree.root))
