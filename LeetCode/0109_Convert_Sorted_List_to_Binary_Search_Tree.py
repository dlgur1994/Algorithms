import sys
read = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertNode(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = self.tail.next
    def printNode(self):
        self.cur = self.head
        while self.cur:
            print(self.cur.val)
            self.cur = self.cur.next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    def insertNode(self,val):
        new_node = TreeNode(val)
        self.cur = self.root
        if self.root is None:
            self.root = new_node
            return
        while True:
            if new_node.val<self.cur.val:
                if self.cur.left==None:
                    self.cur.left = new_node
                    break
                else:
                    self.cur = self.cur.left
            else:
                if self.cur.right==None:
                    self.cur.right = new_node
                    break
                else:
                    self.cur = self.cur.right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getValues(head):
            temp = []
            while head:
                temp.append(head.val)
                head = head.next
            return temp
        def changeOrder():
            if value_list:
                ordered_list.append(int(value_list[len(value_list)//2]))
                value_list.remove(value_list[len(value_list)//2])
                changeOrder()

        value_list = getValues(head)
        ordered_list = []
        output_list = []

        changeOrder()
        for e in ordered_list:
            output_list.append(TreeNode(e))
        return output_list[:2]

input = list(read().rstrip().lstrip('[').rstrip(']').split(','))
linked_list = LinkedList()
for e in input:
    linked_list.insertNode(e)
mod = Solution()

# binary_tree = BinaryTree()
# for e in output_list:
#     binary_tree.insertNode(e)
print(mod.sortedListToBST(linked_list.head))
