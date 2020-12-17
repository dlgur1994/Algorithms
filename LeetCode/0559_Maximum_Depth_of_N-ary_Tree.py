from collections import deque

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

    def addChildren(self, child):
        self.children.append(child)

class Tree:
    def __init__(self):
        self.root = None

    def printNodesDFS(self):
        stack = [self.root]
        nodes = []
        while stack:
            nodes.append(stack.pop())
            for node in nodes:
                print(node.val)
                stack.extend(node.children)
            nodes.clear()

    def printNodesBFS(self):
        queue = deque([self.root])
        nodes = []
        while queue:
            nodes.append(queue.popleft())
            for node in nodes:
                print(node.val)
                queue.extend(node.children)
            nodes.clear()

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        # when root exists
        if root:
            # depth of the root is 1
            depth += 1
            queue = deque([(root,depth)])
            while queue:
                node, dep = queue.popleft()
                for e in node.children:
                    # append node's children and the depth of them to the queue
                    queue.append((e, dep+1))
            # update depth to the deepest child
            depth = dep
        return depth

one = Node("1")
two = Node("2")
three = Node("3")
four = Node("4")
five = Node("5")
six = Node("6")
seven = Node("7")
eight = Node("8")
nine = Node("9")
ten  = Node("10")
elev = Node("11")
twelv = Node("12")
thirt = Node("13")
fourt = Node("14")

one.children = [two, three, four, five]
three.children = [six, seven]
four.children = [eight]
five.children = [nine, ten]
seven.children = [elev]
eight.children = [twelv]
nine.children = [thirt]
elev.children = [fourt]

tree = Tree()
tree.root = one
# tree.printNodesDFS()
# tree.printNodesBFS()

mod = Solution()
print(mod.maxDepth(tree.root))
