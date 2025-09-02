'''
    - Linked List Data Structure Implementations
'''
from node import Node

class LinkedList(object):
    def __init__(self):
        '''
            - Linked List Constructor [ Initializer ]
        '''
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def append(self, value):
        '''
        Adds a new node to the back or end of the Linked List.
        
        Args:
            value (any): The value that will be added to the end of the Linked List.
            
        Returns:
            bool: True the value has been added successfully to the end of the Linked List.
            
        Time Complexity:
            O(1) - appending a new node to the end of the Linked List done in constant time.
        '''
        
        # New node that will be added to the end of the Linked List
        node = Node(value)
        
        # empty Linked List
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            # There is at least one node in the Linked List
            # link tail and the new node
            self.tail.next = node
            # new node becomes the tail or end of the Linked List
            self.tail = node
            
        # increase the Linked List nodes count
        self.length += 1
            
        # a new node has been added successfully
        return True
        
    def print_list(self):
        '''
        Prints the nodes of the Linked List
        
        Args:
            This function does not take any arguments
            and does not return a value    
        '''
        
        # point to the head of the Linked List
        temp = self.head
        
        # Move and print the node as long as 
        # the pointer is not None
        while temp:
            # not end of the Linked List
            if temp.next:
                print(temp.value, end=' ----> ')
            else:
                # tail of the Linked List
                print(temp.value, end=' ----> None')
            temp = temp.next
        print()
        