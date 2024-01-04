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

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert(data)
            return

        new_node = Node(data)
        count = 0
        itr = self.head
        while itr:
            if count == position - 1:
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            count += 1
        else:
            print("Position out of bounds")

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

linked_list.insert_at_position(0, 5)
linked_list.insert_at_position(2, 15)

linked_list.display()