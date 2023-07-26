# main.py
from node import Node
from singly_linked_list import LinkedList
from BinarySearchTree import BinarySearchTree

# Test Task 1
linked_list = LinkedList()
elements = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
for element in elements:
    linked_list.insert(element)

print("Linked List:")
linked_list.display()

# Test Task 2
linked_list.find_max_min()

# Convert linked list to binary search tree and test
bst = BinarySearchTree()
bst.linkedlist_to_bst(linked_list.head)
print("\nBinary Search Tree (Inorder Traversal):")
bst.inorder_traversal(bst.root)
