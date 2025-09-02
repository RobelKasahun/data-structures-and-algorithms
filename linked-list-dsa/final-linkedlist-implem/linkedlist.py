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
        
    def get_head(self):
        '''
        Returns the head or first node of the Linked List
        
        Args:
            Does not take any arguments
            
        Returns:
            node (head): Returns the head node of the Linked List
            
        Time Complexity:
            O(1) - Constant time
        '''
        return self.head.value if self.head else 'None'
    
    def get_tail(self):
        '''
        Returns the end node or tail of the Linked List
        
        Args:
            Does not take any arguments
            
        Returns:
            node (tail): Returns the end node or tail of the Linked List
            
        Time Complexity:
            O(1) - Constant time
        '''
        return self.tail.value if self.tail else 'None'
        
    
    def append(self, value):
        '''
        Adds a new node with the given value to the back or end of the Linked List.
        
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
    
    
    def get_node(self, index):
        '''
        Return the node stored at the given index.
        
        Args:
            index (int): An index where the node is stored.
            
        Returns:
            node (any): The node stored at the given index in the Linked List.
            
        Time Complexity:
            O(n) - pointer must be moved to the node stored at index.
        '''
        
        # index out of range
        if index < 0 or index >= self.length:
            return None
        
        # pointer to the head of the Linked List
        temp = self.head
        
        # iterate index times to reach the node at index
        for _ in range(index):
            temp = temp.next
            
        
        return temp
        
    
    def set_node(self, index, value):
        '''
        Set or update the value of a new positioned at the given index.
        
        Args:
            index (int): An index where the node is stored.
            value (any): A new value to be used to update the node at the given index in the Linked List.
            
        Returns:
            node (any): The updated at the given index
        '''
        
        # index out of range
        if not self.get_node(index):
            return None
        
        node = self.get_node(index)
        node.value = value
        
        return node
    
    
    def pop(self):
        '''
        Remove the tail or node at the end of the Linked List.
        
        Args:
            This function does not take any arguments.
            
        Returns:
            node: Returns the tail or removed node of the Linked List.
            
        Time Complexity:
            O(n) - prev must be moved to a position before the tail node.
                   temp must be moved to the tail of the Linked List.
        '''
        
        temp = self.head
        # empty Linked List
        if not self.head and not self.tail:
            return None
        
        # only one node in the Linked List
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return temp
        
        # point to the head of the Linked List
        temp = self.head
        prev = None
        
        # Move the temp pointer through the Linked List nodes 
        # to have previous and tail nodes
        while temp.next:
            prev = temp
            temp = temp.next
            
        # make previous node the tail of the Linked List
        self.tail = prev
        # Its next pointer must point to None since it is the end of tail of the Linked List
        self.tail.next = None
        # decrease the Linked List node counts
        self.length -= 1
        # return the removed node
        return temp
            
        
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
        