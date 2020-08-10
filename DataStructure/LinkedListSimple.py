class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        dummy = Node(0)
        self.head = dummy
        self.tail = dummy

    def insertNode(self,data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

    def printList(self):
        while self.tail==None:
            print(self.head.data)
            self.head = self.head.next
'''
    def delete(self):

    def search(self):
'''


linkedList = LinkedList()
linkedList.insertNode(5)
linkedList.insertNode(6)
linkedList.printList()
