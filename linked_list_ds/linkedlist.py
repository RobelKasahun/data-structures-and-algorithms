from .node import Node

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
        pass
    
    def print_list(self):
        '''
            Prints all nodes from the List
        '''
        temp = self.head
        while temp:
            if not temp.next:
                print(temp.value, end=' ----> ')
            else:
                print(temp.value, end=' ----> None')
            temp = temp.next
        print()