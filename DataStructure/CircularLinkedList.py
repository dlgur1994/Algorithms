class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.head.next = self.head
        self.num_of_nodes = 1

    def insert_node(self,insert_data):
        new_node = Node(insert_data)
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        cur.next.next = self.head
        self.num_of_nodes += 1

    def print_node(self):
        cur = self.head
        for _ in range(0,self.num_of_nodes):
            print(cur.data)
            cur = cur.next

circularLinkedList = CircularLinkedList()
circularLinkedList.insert_node(3)
circularLinkedList.insert_node(4)
circularLinkedList.insert_node(5)
circularLinkedList.print_node()
