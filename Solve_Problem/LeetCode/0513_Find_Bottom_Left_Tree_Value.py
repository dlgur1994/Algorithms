from collections import deque
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
    def insertNode(self,node,left_node,right_node):
        if self.root==None:
            self.root = node
        if left_node.val != 'null':
            node.left = left_node
        if right_node.val != 'null':
            node.right = right_node

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root == None:
            return
        visited = []
        queue = deque([(root,0)])
        while queue:
            node,height = queue.popleft()
            if len(visited)<=height:
                visited.append([node.val])
            else:
                visited[height].append(node.val)
                # visited[height].extend(node.val) --> when I use my input, the values were strings, so I used 'extend'
            if node.left:
                queue.append((node.left,height+1))
            if node.right:
                queue.append((node.right,height+1))
        return visited[-1][0]

input = list(map(TreeNode,read().rstrip().lstrip('[').rstrip(']').split(',')))
binary_tree = BinaryTree()
for i in range(len(input)//2):
    binary_tree.insertNode(input[i],input[(2*i)+1],input[(2*i)+2])
mod = Solution()
print(mod.findBottomLeftValue(binary_tree.root))
