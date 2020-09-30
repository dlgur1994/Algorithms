import sys
read = sys.stdin.readline

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self,data):
        new_node = TreeNode(data)
        self.cur = self.root
        if self.root == None:
            self.root = new_node
        else:
            while True:
                if new_node.data < self.cur.data:
                    if self.cur.left == None:
                        self.cur.left = new_node
                        break
                    else:
                        self.cur = self.cur.left
                else:
                    if self.cur.right == None:
                        self.cur.right = new_node
                        break
                    else:
                        self.cur = self.cur.right

    # def print_node(self, node):
    #     if node == None:
    #         pass
    #     else:
    #         print (node.data)
    #         self.print_node(node.left)
    #         self.print_node(node.right)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                pass
            else:
                dfs(root.left)
                elements.append(root.data)
                dfs(root.right)

        def createBST(elist):
            root_node = TreeNode(elist[0])
            new_root = root_node
            elist.pop(0)
            for e in elist:
                new_root.right = TreeNode(e)
                new_root = new_root.right
            return new_root

        elements = []
        dfs(root)
        return createBST(elements)

input = list(read().rstrip().rstrip(']').lstrip('[').split(','))
tree_node = BinaryTree()
for e in input:
    if e == 'null':
        continue
    tree_node.insert_node(int(e))
mod = Solution()
print(mod.increasingBST(tree_node.root))
