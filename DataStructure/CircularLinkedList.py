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

    def search_node(self,search_data):
        cur = self.head.next
        while cur != self.head:
            if(cur.data == search_data):
                print('found')
                return
            cur = cur.next
        print('not found')

    def delete_node(self, delete_data):
        cur = self.head.next
        prev = self.head
        while cur != self.head:
            if cur.data == delete_data:
                prev.next = prev.next.next
                self.num_of_nodes -= 1
            cur = cur.next
            prev = prev.next

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

circularLinkedList.search_node(3)
circularLinkedList.search_node(4)
circularLinkedList.search_node(5)
circularLinkedList.search_node(6)

circularLinkedList.delete_node(3)
circularLinkedList.delete_node(4)
circularLinkedList.delete_node(5)
circularLinkedList.print_node()
