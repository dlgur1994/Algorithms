from collections import deque
from typing import List
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
    def insertNode(self,cen_node,left_node,right_node):
        if self.root is None:
            self.root = cen_node
        if left_node and left_node.val!='null':
            cen_node.left = left_node
        if right_node and right_node.val!='null':
            cen_node.right = right_node

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        visited = []
        queue = deque([(root,0)])
        while queue:
            node,height = queue.popleft()
            if height>=len(visited):
                visited.append([node.val])
            else:
                visited[height].append(node.val)
            if node.left:
                queue.append((node.left,height+1))
            if node.right:
                queue.append((node.right,height+1))
        return list(reversed(visited))


input = list(map(TreeNode,read().rstrip().lstrip('[').rstrip(']').split(',')))
binary_tree = BinaryTree()
for i in range(len(input)//2):
    binary_tree.insertNode(input[i],input[2*i+1],input[2*i+2])
mod = Solution()
print(mod.levelOrderBottom(binary_tree.root))
