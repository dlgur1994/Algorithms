class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

    def insertNode(self,data):
        newNode = Node(data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def printNode(self):
        cur = self.head
        while cur != self.tail.next:
            print(cur.data)
            cur = cur.next

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insertNode(3)
doublyLinkedList.insertNode(4)
doublyLinkedList.printNode()
