class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = new_node

    def delete(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next

        print(f"Element {value} not found in the linked list")

    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next
        print("None")

linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

linked_list.display()

linked_list.delete(10)
linked_list.delete(30)

linked_list.display()