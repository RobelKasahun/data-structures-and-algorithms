from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def is_empty(self):
        '''
            Checks whether the List is empty or not

            Returns:
                bool: True if the List is empty, False otherwise
        '''
        return (not self.head and not self.tail)
        
    def append(self, value):
        '''
            Add the given node to the end of the Linked List
            
            Args:
                value (any): value will be added to the end of the Linked List
                
            Returns:
                bool: True: The node added to the end of the List successfully
        '''
        
        node = Node(value)
        
        # List is empty
        if self.is_empty():
            # add node and head and tail will point to the node
            self.head = self.tail = node
        else:
            # There is one or more nodes in the List
            self.tail.next = node
            self.tail = node
        
        # increase the node counts by one
        self.length += 1
        
        return True
    
    def get_head(self):
        '''
            Returns the head node of the List
            
            Returns:
                node (any): The head node of the List
        '''
        return self.head
    
    def get_tail(self):
        '''
            Returns the tail node of the List
            
            Returns:
                node (any): The tail node of the List
        '''
        return self.tail
    
    def pop(self):
        removed_node = None
        
        # List is empty
        if self.is_empty():
            return None
        
        # only one node in the List
        if self.length == 1:
            removed_node = self.head
            self.head = self.tail = None
            self.length -= 1
            
            return removed_node
        
        # List has more than 1 node
        temp = self.head
        prev = self.head
        
        while temp.next:
            prev = temp
            temp = temp.next
            
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        
        return temp
    
    def prepend(self, value):
        '''
            Add a node to the beginning or at the head of the List
            
            Returns:
                bool: The given node has successfully been added to the beginning of the List
        '''
        node = Node(value)
        
        # The list is empty, thus add the node and head and tail points to it
        if self.is_empty():
            self.head = self.tail = node
        else:
            # There is at least one node in the List
            node.next = self.head
            self.head = node
            
        self.length += 1
        
        return True
    
    def pop_first(self):
        '''
            Remove the head node of the List
            
            Returns:
                node(any): The removed node from the beginning of the List
        '''
        temp = None
        if self.is_empty():
            return None
        
        # List has one or more nodes
        if self.length == 1:
            temp = self.head
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        
        self.length -= 1
        temp.next = None
        return temp
    
    def get_node(self, index):
        '''
            Return the node stored at the given position
            
            Returns:
                node(any): The node at the given position
        '''
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        
        return temp
    
    def set_node(self, index, value):
        '''
            Update the node at the given position
            
            Returns:
                node(any): The updated node at the given position
        '''
        if index < 0 or index >= self.length:
            return False
        
        temp = self.get_node(index)
        temp.value = value
        
        return temp
    
    def insert(self, index, value):
        '''
            Inserts a node before the given index position
            
            Returns:
                bool: True if the node inserted successfully, False otherwise
        '''
        if index < 0 or index > self.length:
            return False
        
        # add at the beginning of the List
        if index == 0:
            return self.prepend(value)
        
        # Add at the end of the List
        if index == self.length:
            return self.append(value)
        
        node = Node(value)
        # insert in the middle
        temp = self.get_node(index)
        prev = self.get_node(index - 1)
        
        node.next = temp
        prev.next = node
        self.length += 1
        
        return True
    
    def remove(self, index):
        '''
            Removes the node at the given index position
            
            Returns:
                node(any): the removed node
        '''
        if not self.get_node(index):
            return None
        
        # remove the head node
        if index == 0:
            return self.pop_first()
        
        # remove the tail node
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get_node(index)
        prev = self.get_node(index - 1)
        
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        # empty list
        if self.is_empty():
            return None
        
        # swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    
    def print_list(self):
        '''
            Prints all nodes from the List
        '''
        temp = self.head
        while temp:
            if temp.next:
                print(temp.value, end=' ----> ')
            else:
                print(temp.value, end=' ----> None')
            temp = temp.next
        print()