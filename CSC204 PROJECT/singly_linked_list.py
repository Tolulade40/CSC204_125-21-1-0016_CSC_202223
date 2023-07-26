# linkedlists.py
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
# linkedlists.py (add this method to the LinkedList class)
    def find_max_min(self):
        if not self.head:
            print("The list is empty.")
            return None

        current = self.head
        max_data = min_data = current.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        print("Maximum data:", max_data)
        print("Minimum data:", min_data)
#task 3
    def sort_list(self):
        # Convert linked list to a list
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        # Sort the list
        elements.sort()

        # Create a new linked list with sorted elements
        sorted_list = LinkedList()
        for element in elements:
            sorted_list.insert(element)

        return sorted_list

    def enqueue(self, data):
        self.insert(data)

    def dequeue(self):
        if not self.head:
            print("Queue is empty.")
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    def display_queue(self):
        self.display()
