from node import Node

class LinkedList:
    ''' *** Constructor [ Initializer ] *** '''
    def __init__(self):
        '''
            LinkedList: Constructor
            Set head and tail to None
            and length to 0
        '''
        self.head = self.tail = None
        self.length = 0
        
    ''' *** is_empty() *** '''
    def is_empty(self):
        '''
            Checks and returns boolean value if the LinkedList is empty or not
            Returns:
                bool: True if the LinkedList is empty, false otherwise
        '''
        return not self.head
    
    ''' *** prepend() *** '''
    def prepend(self, value):
        # create a new node
        node = Node.create_node(self, value)
        # empty List
        if self.is_empty():
            self.head = self.tail = node
        else:
            # List has one or more nodes
            node.next = self.head
            self.head = node
            
        self.length += 1
        # a new node has been added to the front of the List
        return True
        
    ''' *** append(value) *** '''
    def append(self, value):
        '''
            Adds a new node to the end of a LinkedList
            Returns:
                bool(True): The new node has been added to the end of the LinkedList successfully
        '''
        # create a new node
        node = Node.create_node(self, value)
        
        # LinkedList is empty [ no nodes ]
        if self.is_empty():
            # head and tail points to the new node
            # because it is the only node in the LinkedList
            self.head = self.tail = node
        else:
            # make the tail point to the new node
            self.tail.next = node
            # make the new node the tail of the LinkedList
            self.tail = node
        
        # increment the node counts
        self.length += 1
        
        # Successfully added to the end of the LinkedList
        return True
    
    ''' *** pop_first() *** '''
    def pop_first(self):
        temp_node = None
        
        # empty List
        if self.is_empty():
            return None
        
        # There is only one node in the List
        if self.length == 1:
            temp_node = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp_node
        
        # when there are two or more nodes in the List
        temp_node = self.head
        self.head = self.head.next
        self.length -= 1
        
        temp_node.next = None
        
        return temp_node
        
    ''' *** pop_last() *** '''
    def pop_last(self):
        '''
            Remove the tail or last node of a Linked List
            Returns:
                node(any): Returns the the node removed from the end of the Linked List
        '''
        # empty Linked List
        if self.is_empty():
            return None
        
        # List has only one node
        if self.length == 1:
            temp_node = self.head = self.tail
            # remove the node
            self.head = self.tail = None
            # count the removed nodes
            self.length -= 1
            # return the removed node
            return temp_node
        
        temp_node = self.head
        prev_node = self.head
        
        # as long as the current node not pointing to None
        while temp_node.next:
            # node before the tail node
            prev_node = temp_node
            temp_node = temp_node.next
            
        # make the prev node tail of the List
        self.tail = prev_node
        self.tail.next = None
        
        self.length -= 1
        
        return temp_node
    
    def get_node(self, index):
        '''
            Returns the node positioned at the index
            Returns:
                node(any): The node at index
        '''
        # index out of bounds
        if index < 0 or index >= self.length:
            return None
        
        # move the ponter to the node at the given index
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        
        # return the node at the given index
        return temp_node
    
    def set_node(self, index, value):
        '''
            Update the node at the given index
        '''
        # index out of bounds
        if not self.get_node(index):
            return False
        
        # get the node at the given index
        node = self.get_node(index)
        
        # update the value of the node at the given index
        node.value = value
        
        # the node at the given index has been updated
        return True
    
    def insert(self, index, value):
        '''
            Insert the given node at the given index
            
            Returns:
                bool: True if inserted successfully, false otherwise
        '''
        if index < 0 or index > self.length:
            return False
        
        # insert the node at the head of the List
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            # insert the node at the tail of the List
            return self.append(value)
        else:
            # insert the node in the middle of the List
            prev = self.get_node(index - 1)
            node = Node.create_node(self, value)
            node.next = prev.next
            prev.next = node
            self.length += 1
            
            return True
        
    def remove(self, index):
        '''
            Removes the node at the given index
            
            Returns:
                node(any): Returns the removed node, None otherwise
        '''
        # index out of bounds
        if not self.get_node(index):
            return None
        
        # remove the node at the head of the List
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            # remove the node at the tail of the List
            return self.pop_last()
        
        # remove the node in the middle of the List
        prev = self.get_node(index - 1)
        # temp = self.get_node(index)
        temp = prev.next    # more efficient
            
        prev.next = temp.next
        temp.next = None
            
        self.length -= 1
            
        return temp
    
    ''' *** reverse() *** '''
    def reverse(self):
        '''
            Reverse the existing List
        '''
        # empty List
        if self.is_empty():
            return None
        
        # reverse head and tail
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node
        
        after = temp_node.next
        before = None
        
        for _ in range(self.length):
            after = temp_node.next
            temp_node.next = before
            before = temp_node
            temp_node = after
            
    
    def clear(self):
        '''
            Clears or delete all the nodes in the List
            Leaves the List empty with 0 nodes
        '''
        if not self.is_empty():
            for _ in range(self.length):
                self.pop_last()
            
    
    ''' *** print_linkedlist() *** '''
    def print_linkedlist(self):
        '''
            Prints all the nodes in the LinkedList to the console pane
        '''
        # temporary head
        temp_head = self.head
        # print nodes as long as the current node is not None
        while temp_head:
            if temp_head.next:
                print(temp_head.value, end=' ----> ')
            else:
                print(temp_head.value, end=' ----> None')
            temp_head = temp_head.next
        print()