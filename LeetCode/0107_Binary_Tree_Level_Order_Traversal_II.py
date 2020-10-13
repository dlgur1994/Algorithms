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
        def bfs(_root):
            visited = []
            queue = deque([_root])
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return visited

        def groupNodes(nodes):
            cnt = 0
            while True:
                temp = []
                for _ in range(int(2**cnt)):
                    if len(nodes)==0:
                        output.append(temp)
                        return
                    temp.append(int(nodes[0]))
                    nodes.pop(0)
                output.append(temp)
                cnt += 1

        output = []
        node_list = bfs(root)
        groupNodes(node_list)
        return list(reversed(output))


input = list(map(TreeNode,read().rstrip().lstrip('[').rstrip(']').split(',')))
binary_tree = BinaryTree()
for i in range(len(input)//2):
    binary_tree.insertNode(input[i],input[2*i+1],input[2*i+2])
mod = Solution()
print(mod.levelOrderBottom(binary_tree.root))
