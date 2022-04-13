import sys
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    
    def insertNode(self, center, left, right):
        if self.root == None:            
            self.root = center
            self.root.val = int(self.root.val)
        if left.val != 'null':
            left.val = int(left.val)
            center.left = left
        if right.val != 'null':
            right.val = int(right.val)
            center.right = right

    def printNode(self, node):
        print(node.val)
        if node.left:
            self.printNode(node.left)
        if node.right:
            self.printNode(node.right)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        ans = [[root.val]]
        nodes = [root]
        cnt = 0

        parents = [[nodes[cnt]]]
        while True:
            children = []
            vals = []
            if len(parents) == cnt:
                break
            
            for parent in parents[cnt]:
                if parent.left:
                    children.append(parent.left)
                    vals.append(parent.left.val)
                if parent.right:
                    children.append(parent.right)
                    vals.append(parent.right.val)

            if children == []:
                return ans

            parents.append(children)
            ans.append(vals)
            cnt += 1

nodes = list(map(TreeNode, sys.stdin.readline().rstrip().split(',')))
tree = Tree()
for i in range(len(nodes)//2):
    tree.insertNode(nodes[i], nodes[2*i+1], nodes[2*i+2])
# tree.printNode(tree.root)

mod = Solution()
print(mod.levelOrder(tree.root))