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
        
    def is_empty(self):
        '''
        Checks if the Linked List is empty or not.
        
        Args:
            Does not take any arguments.
            
        Returns:
            bool: True if the Linked List is empty. Otherwise, False.
            
        Time Complexity:
            O(1) - Constant time.
        '''
        return not self.head and not self.tail
        
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
            O(1) - ( Constant time ) appending a new node to the end of the Linked List done in constant time.
        '''
        
        # New node that will be added to the end of the Linked List
        node = Node(value)
        
        # empty Linked List
        if self.is_empty():
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
    
    
    def get(self, index):
        '''
        Return the node stored at the given index.
        
        Args:
            index (int): An index where the node is stored.
            
        Returns:
            node (any): The node stored at the given index in the Linked List.
            
        Time Complexity:
            O(n) - ( Linear time ) pointer must be moved to the node stored at index.
        '''
        
        # empty Linked List
        if self.is_empty():
            return None
        
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
            bool (any): The node at the given index has been updated.
            
        Time Complexity:
            O(n) - Linear time.
        '''
        
        # get the node at the given index
        temp = self.get(index)
        
        # index out of range
        if not temp:
            return False
        
        # update the node at the given index
        temp.value = value
        
        # return the updated node
        return True
    
    
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
        if self.is_empty():
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
        # decrease the Linked List nodes count
        self.length -= 1
        # return the removed node
        return temp
    
    
    def prepend(self, value):
        '''
        Adds a new node to the beginning of the Linked List.
        
        Args:
            value (any): The value to be added to the beginning or head of the Linked List.
            
        Returns:
            bool: Return true when a new node added to the beginning of the Linked List.
            
        Time Complexity:
            O(1) - Constant time.
        '''
        
        # The node to be added to the beginning of the Linked List
        node = Node(value)
        
        # empty Linked List
        if self.is_empty():
            self.head = self.tail = node
        else:
            # There is at least one node in the Linked List
            node.next = self.head
            self.head = node
        
        # increase the nodes count
        self.length += 1
        
        return True
    
    
    def pop_first(self):
        '''
        Removes the head or node at the beginning of the Linked List.
        
        Args:
            Does not take arguments
            
        Returns:
            node (any): The removed or head of the Linked List.
            
        Time Complexity:
            O(1) - Constant time.
        '''
        
        temp = self.head
        
        # empty Linked List
        if not self.head or not self.tail:
            return None
        
        # only one node in the Linked List
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return temp
        
        # There are two or more nodes in the Linked List
        # make the next node as the head of the Linked List
        self.head = self.head.next
        # decrease the nodes count 
        self.length -= 1
        # head of the node must point to None to break the link
        temp.next = None
        
        # return the removed head node
        return temp
    
    
    def insert(self, index, value):
        '''
        Inserts a new node into the Linked List before the given index.
        
        Args:
            index (int): The index where the new node will be stored.
            value: (any): New node that will be inserted at the given index.
            
        Returns:
            Returns true to indicate the new node has been inserted at the given index.
            
        Time complexity:
            O(1) - Constant time inserting on both ends of the Linked List.
            O(n) - Linear time: inserting in the middle of the Linked List.
        '''
        
        # index out of range
        if index < 0 or index > self.length:
            return False
        
        # insert at the beginning of the Linked List
        if index == 0:
            return self.prepend(value)
        
        # Insert at the end of the Linked List        
        if index == self.length:
            return self.append(value)

        # Insert somewhere in the middle of the Linked List
        node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        
        node.next = temp
        prev.next = node
        
        self.length += 1
        
        return True
    
    
    def remove(self, index):
        '''
        Removes a node at the specified or given index.
        
        Args:
            index (int): The position of the node that is going to be deleted or removed from the Linked List.
            
        Returns:
            node (any): returns the removed node.
            
        Time Complexity:
            O(1) - Constant time on removing the first node
            O(n) - Linkear time on removing the tail node
            O(n) - Linear time on removing a node somewhere from the middle
            Overall time complexity
                - O(1) + O(n) + (n)
                - O(1) + O(2n)
                - O(1) + O(n)
                - O(n)
        '''
        
        # empty Linked List
        if self.is_empty():
            return None
        
        # get the node at index
        temp = self.get(index)
        
        if not temp:
            # index out of range
            return None
        
        # remove the first node
        if index == 0:
            return self.pop_first()
        
        # remove the tail node or last node
        if index == self.length - 1:
            return self.pop()
        
        # remove a node somewhere in the middle
        
        prev = self.get(index - 1)
        prev.next = temp.next
        
        temp.next = None
        
        self.length -= 1
        
        return temp
    
    
    def reverse(self):
        '''
        Reverse a Linked List.
        
        Args:
            Does not take any arguments.
            
        Returns:
            Does not return a value.
            
        Time Complexity:
            O(n) - Linear time.
        '''
        
        # empty Linked List
        if self.is_empty():
            print(f'Empty Linked List cannot be reversed.')
            
        # swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        # set before and after to None
        after = None
        before = None
        
        for _ in range(self.length):
            # point after to node next temp
            after = temp.next
            # flip the pointer to before
            temp.next = before
            # move before to point to the node that temp is pointing
            before = temp
            # move temp to the node pointed by after
            temp = after
            
    def find_mid_node(self):
        '''
        Find the middle node of a Linked List.
        
        Args:
            Does not take any arguments.
            
        Returns:
            node (any): the middle node.
            
        Time Complexity:
            O(n) - Linear time.
        '''
        # initialize fast and slow to the head of the Linked List
        fast = self.head
        slow = self.head
        
        # increment slow by one node and fast by two nodes
        # as long as the fast is not None
        while fast:
            if not fast.next:
                break
            fast = fast.next.next
            slow = slow.next
    
        # middle node
        return slow
    
    def has_loop(self):
        '''
        Check if a Linked List has a loop.
        
        Args:
            Does not take any arguments.
            
        Returns:
            bool: True if the Linked List has a loop. Otherwise, False.
            
        Time Complexity:
            O(n) - Linear time.
        '''
        # set slow and fast to the head of the Linked List
        slow = self.head
        fast = self.head
        
        is_loop = False
        
        # iterate through the Linked List as long as fast is not None
        while fast:
            # move slow one step at a time
            slow = slow.next
            # move fast two steps at a time
            fast = fast.next.next
            
            # End of Linked List
            if not fast or not fast.next:
                break
            
            # determine if fast and slow pointing to the same node
            if fast.value == slow.value:
                is_loop = True
                break
        # return True if the Linked List has a loop
        # False if the Linked List does not have a loop
        return is_loop
    
    def find_kth_node(self, k):
        # Solution using length
        # index out of range
        # if k < 0 or k > self.length:
        #     return None
        # if k == 1:
        #     return self.tail
        
        # if k == self.length:
        #     return self.head
        
        # kth_node = self.head
        
        # for _ in range(self.length - k):
        #     kth_node = kth_node.next
            
        
        # return kth_node
        
        # Solution without using length
        slow = self.head
        fast = self.head
        
        # move fast to k position
        for _ in range(k):
            if not fast:
                return None
            fast = fast.next
            
        # move slow as long as fast is not None
        while fast:
            slow = slow.next
            fast = fast.next
            
        # the kth node
        return slow
                
        
        
    def print_list(self):
        '''
        Prints the nodes of the Linked List
        
        Args:
            This function does not take any arguments
            and does not return a value    
            
        Returns:
            This function does not return a value
            
        Time Complexity:
            O(n) - Linear time
        '''
        
        # Empty Linked List
        if self.is_empty():
            print(f'*** Empty Linked List ***')
        
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
        